# AUTOMATED-REPORT-GENERATION
**Name:** [Shriraj Dharmadhikari]  
**Company:** CODTECH IT SOLUTIONS  
**ID:** [CT08PEP]  
**Domain:** PYTHON PROGRAMMING  
**Duration:** [Jan 25th to Feb 25th]  

---

### Overview of the Project
- This project focuses on creating an automated report generation tool using Python.
- The script reads data from a CSV file, performs basic analysis, and generates a professional PDF report with summarized insights using the ReportLab library.

### Objective
- Automate the process of analyzing sales data.
- Generate a clear and concise PDF report for business insights.

### Key Activities
- **Reading data**: Load data from a CSV file using the `csv` module.
- **Data Analysis**:
  - Calculate count, sum, average, max, and min of numeric columns.
- **PDF Report Generation**:
  - Create a formatted PDF containing the calculated results.
  - Include a title and organized content for better readability.

### Technologies Used
- **Python**: The primary programming language for the task.
- **Libraries**:
  - `csv`: For reading and processing data from the CSV file.
  - `reportlab`: For creating and formatting PDF reports.

### Scope
- Automates manual calculations and report creation.
- Provides business insights in a portable and shareable PDF format.
- Can be easily adapted to handle other types of data in the future.

### Advantages
- Saves time by automating repetitive tasks.
- Ensures accuracy in calculations and reporting.
- Generates professional, shareable PDF reports.

### Disadvantages
- Limited to basic numeric data analysis.
- Requires the CSV file to follow a specific format.
- Report customization is minimal without additional enhancements.

### Key Insights
- Automating repetitive tasks like report generation increases efficiency.
- Libraries like ReportLab are simple yet effective for creating PDF documents.

### Future Improvements
- Add data visualization like charts or graphs for better insights.
- Include error handling for a wider range of file formats and data inconsistencies.
- Develop a user-friendly interface (e.g., a web or desktop app).

### Code Explanation
1. **Reading Data**:
   - The `read_csv` function reads data from a CSV file using Python's `csv` module.
   - Ensures all records are loaded into a list of dictionaries for further processing.
   - Handles missing files gracefully with an error message.

2. **Data Analysis**:
   - The `analyze_data` function calculates:
     - Count of numeric values.
     - Total sum of numeric values.
     - Average, maximum, and minimum of each numeric column.
   - Includes error handling for invalid data values.

3. **PDF Report Generation**:
   - The `generate_pdf_report` function creates a PDF file using the ReportLab library:
     - Adds a title: "Automated Data Analysis Report".
     - Displays column-wise statistical insights in a clean, readable format.
     - Saves the report as `Report1.pdf`.

4. **Main Functionality**:
   - The script ties everything together:
     - Reads the data from the CSV file.
     - Analyzes the data to calculate totals and averages.
     - Generates a PDF report if valid data exists.
     - Skips report generation if no numeric data is found.

### Sample Output (Report Format)
- **Title**: "Automated Data Analysis Report"
- **Column-wise Summary**:
  - Count: Displays the number of numeric values.
  - Sum: Displays the total sum of numeric values.
  - Average: Displays the average of numeric values.
  - Max: Displays the highest value.
  - Min: Displays the lowest value.
  
### Otuput



### Contact
- **Name**: [Shriraj Dharmadhikari]
- **Company**: CODTECH IT SOLUTIONS
- **Email**: [shrirajdharmadhikari@gmail.com]
