import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def read_csv(file_path):
    """Reads CSV data and returns a list of dictionaries."""
    data = []
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return data

def analyze_data(data):
    """Analyzes numeric data and generates summary statistics."""
    summary = {}

    if not data:
        return summary  

    for key in data[0]:  
        values = []
        for row in data:
            try:
                values.append(float(row[key]))  
            except ValueError:
                continue  

        if values:
            summary[key] = {
                "Count": len(values),
                "Sum": round(sum(values), 2),
                "Average": round(sum(values) / len(values), 2),
                "Max": round(max(values), 2),
                "Min": round(min(values), 2)
            }
    
    return summary

def generate_pdf_report(summary, output_path):
    """Generates a PDF report with the analyzed data."""
    pdf = canvas.Canvas(output_path, pagesize=letter)
    pdf.setTitle("Data Analysis Report")

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 750, "Automated Data Analysis Report")

    pdf.setFont("Helvetica", 12)
    y_position = 720  

    if not summary:
        pdf.drawString(50, y_position, "No numeric data found for analysis.")
    else:
        for column, stats in summary.items():
            pdf.drawString(50, y_position, f"Column: {column}")
            y_position -= 20
            for key, value in stats.items():
                pdf.drawString(70, y_position, f"{key}: {value}")
                y_position -= 20
            y_position -= 10  

    pdf.save()
    print(f"PDF report saved as {output_path}")

def main():
    input_file = input_file = r"C:\MSC-fy\Internship\Task2\data.csv"
    output_file = "Report.pdf"

    data = read_csv(input_file)
    summary = analyze_data(data)

    generate_pdf_report(summary, output_file)

if __name__ == "__main__":
    main()
