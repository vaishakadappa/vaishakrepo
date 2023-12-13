import pandas as pd
import requests
import pdfkit

excel_file = 'TAIY_1.5K_28Sp.xlsx'
df = pd.read_excel(excel_file)

# Use pdfkit's included wkhtmltopdf binary
pdfkit_config = pdfkit.configuration(wkhtmltopdf=pdfkit.config.wkhtmltopdf)

for index, row in df.iterrows():
    html_link = row['HTML LINK']  # Replace with the actual column name

    response = requests.get(html_link)
    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve HTML content for row {index}")
        continue
    pdf_filename = f'output_{index}.pdf'

    # Convert HTML to PDF with specified options
    pdfkit.from_file(html_content, pdf_filename, configuration=pdfkit_config)
    print(f'PDF generated for row {index}')
