import pandas as pd
import requests
import pdfkit

# Load the Excel file
excel_file = "urls.xlsx"
df = pd.read_excel(excel_file)

# Path to wkhtmltopdf executable (required for pdfkit)
# You can download it here: https://wkhtmltopdf.org/downloads.html
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Change this to the path on your system

# Configure pdfkit with the path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Function to convert HTML to PDF
def convert_html_to_pdf(url, output_pdf):
    try:
        # Download HTML content
        response = requests.get(url)
        html_content = response.text

        # Convert HTML to PDF
        pdfkit.from_string(html_content, output_pdf, configuration=config)
        print(f"Converted {url} to {output_pdf}")
    except Exception as e:
        print(f"Error converting {url} to PDF: {str(e)}")

# Iterate through rows and convert to PDF
for index, row in df.iterrows():
    url = row['HTML LINK']  # Assuming 'URL' is the column name with the HTML links
    output_pdf = f"output_{index}.pdf"  # Change the naming convention as needed
    convert_html_to_pdf(url, output_pdf)
