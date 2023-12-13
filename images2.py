from PIL import Image

from reportlab.pdfgen import canvas

import os

 

def convert_image_to_pdf(image_path, pdf_path):

    image = Image.open(image_path)

    pdf = canvas.Canvas(pdf_path, pagesize=image.size)

    pdf.drawImage(image_path, 0, 0, width=image.width, height=image.height)

    pdf.save()

 

def convert_images_to_pdfs(input_folder, output_folder):

    # Ensure the output folder exists

    if not os.path.exists(output_folder):

        os.makedirs(output_folder)

 

    # Get a list of all image files in the input folder

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

 

    # Convert each image to a separate PDF

    for image_file in image_files:

        image_path = os.path.join(input_folder, image_file)

        pdf_name = os.path.splitext(image_file)[0] + '.pdf'

        pdf_path = os.path.join(output_folder, pdf_name)

 

        convert_image_to_pdf(image_path, pdf_path)

 

if __name__ == "__main__":

    input_folder = r"C:\vaishak\images"

    output_folder = r"C:\vaishak\pdfs"

    convert_images_to_pdfs(input_folder, output_folder)