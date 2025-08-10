# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SANKET ANIL SHELAR

*INTERN ID*: CTO4DH1987

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

# 📊 DataInsightPro: Automated CSV Analysis & PDF Report Generator

This Python project reads a CSV dataset, computes summary statistics, visualizes average values, and generates a professional PDF report with optional branding. It's ideal for quick insights and presentations.

## 🚀 Features

- ✅ Reads and cleans numeric data from a CSV file
- 📈 Calculates average, maximum, and minimum for each column
- 📊 Generates a bar chart of column-wise averages
- 📝 Saves metrics to a JSON file
- 📄 Creates a branded PDF report with summary and chart
- 🖼️ Optional logo integration for professional touch

## 🧰 Tech Stack

| Library         | Purpose                          |
|----------------|----------------------------------|
| `csv`           | Reading tabular data             |
| `json`          | Saving metrics in structured format |
| `matplotlib`    | Creating bar chart visualization |
| `reportlab`     | Generating PDF report            |
| `statistics`    | Computing mean values            |
| `os`, `datetime`| File handling and timestamping   |

## 📁 File Structure
project sanket/ ├── dataset.csv ├── metrics.json ├── mean_chart.png ├── InsightReport_<timestamp>.pdf └── assets/ └── brand_logo.png  # Optional

## 🛠️ How to Run

1. Place your CSV file as `dataset.csv` inside the project folder  
2. (Optional) Add a logo image at `assets/brand_logo.png`  
3. Run the script:
   ```bash
   python generate_report.py

## OUTPUT

