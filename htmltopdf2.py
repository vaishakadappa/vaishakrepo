
from pyppeteer import launch
import openpyxl
from weasyprint import HTML



# Define a function to convert HTML to PDF
def convert_html_to_pdf(html_url, pdf_filename):
    try:
        HTML(string=html_url).write_pdf(pdf_filename)
        print(f"Converted {html_url} to {pdf_filename}")
    except Exception as e:
        print(f"Failed to convert {html_url} to PDF: {e}")

# Load the Excel file
excel_file = 'TAIY_1.5K_28Sp.xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active  # Assuming you're working with the active sheet

# Define the column where HTML URLs are located
url_column = 'HTML LINK'  # Change this to the appropriate column letter

# Iterate through rows and convert HTML to PDF
for row in sheet.iter_rows(min_row=2, values_only=True):
    html_url = row[1]  # Assuming the URLs are in the first column (column A)
    pdf_filename = f"{row[1].replace('http://', '').replace('https://', '')}.pdf"  # Creating a PDF filename

    convert_html_to_pdf(html_url, pdf_filename)

# Save the workbook (optional)
workbook.save('output_excel_file.xlsx')

# Close the Excel file
workbook.close()
