import csv
import json
import os
from statistics import mean
from datetime import datetime
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

# --- Setup paths ---
base_dir = r"C:\Users\SONAL\OneDrive\Desktop\project sanket"
csv_file = os.path.join(base_dir, "dataset.csv")
json_file = os.path.join(base_dir, "metrics.json")
logo_file = os.path.join(base_dir, "assets", "brand_logo.png")  # Optional logo
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
pdf_file = os.path.join(base_dir, f"InsightReport_{timestamp}.pdf")
chart_file = os.path.join(base_dir, "mean_chart.png")

# --- Validate CSV path ---
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"❌ CSV file not found at: {csv_file}")
else:
    print(f"✅ CSV file found: {csv_file}")

# --- Read CSV Data ---
headers, data_rows = [], []
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        cleaned_row = []
        for val in row:
            try:
                cleaned_row.append(float(val))
            except ValueError:
                cleaned_row.append(0.0)
        data_rows.append(cleaned_row)

# --- Compute Summary Statistics ---
columns = list(zip(*data_rows))
metrics = {
    headers[i]: {
        "Average": round(mean(col), 2),
        "Maximum": max(col),
        "Minimum": min(col)
    } for i, col in enumerate(columns)
}

# --- Save Metrics to JSON ---
with open(json_file, "w") as jf:
    json.dump(metrics, jf, indent=4)

# --- Create Bar Chart ---
averages = [stats["Average"] for stats in metrics.values()]
plt.figure(figsize=(10, 5))
plt.bar(headers, averages, color='mediumseagreen')
plt.title("Average Values per Column")
plt.ylabel("Mean")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(chart_file)
plt.close()

# --- Generate PDF Report ---
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Header
c.setFont("Helvetica-Bold", 18)
c.drawString(50, height - 50, "📈 DataInsightPro Report")
c.setFont("Helvetica", 12)
c.drawString(50, height - 75, f"Generated: {datetime.now().strftime('%d %b %Y, %I:%M %p')}")

# Logo (if available)
try:
    if os.path.exists(logo_file):
        c.drawImage(ImageReader(logo_file), width - 120, height - 90, width=60, preserveAspectRatio=True)
except Exception as e:
    print(f"⚠️ Logo error: {e}")

# Metrics Summary
y = height - 120
for col, stats in metrics.items():
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, f"Column: {col}")
    y -= 20
    c.setFont("Helvetica", 11)
    for label, value in stats.items():
        c.drawString(70, y, f"{label}: {value}")
        y -= 15
    y -= 10

# Chart
try:
    if os.path.exists(chart_file):
        c.drawImage(chart_file, 50, y - 220, width=400, preserveAspectRatio=True)
except Exception as e:
    print(f"⚠️ Chart error: {e}")

# Finalize
c.save()
print(f"✅ Unique PDF created: {pdf_file}")