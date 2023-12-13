from PIL import Image
from fpdf import FPDF
import os
import datetime


input_dir="C:\\vaishak\\images"
output_dir="C:\\vaishak\\newpdfs"
log_file="C:\\vaishak\\logfile.txt"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


pdf=FPDF()

with open(log_file,"w") as log:
    log.write("Image to pdf conversion log \n")
    log.write(f"date and time :{datetime.datetime.now()}\n")

image_files = [f for f in os.listdir(input_dir) if f.endswith((".jpg", ".png", ".jpeg"))]
 
for image_file in image_files:
    image_path = os.path.join(input_dir, image_file)
    pdf_path = os.path.join(output_dir, os.path.splitext(image_file)[0] + ".pdf")
 
    # Open and process the image
 
    image = Image.open(image_path)
    pdf.add_page()
    pdf.image(image_path, x=10, y=10, w=190)
    
    pdf.output(pdf_path)
 
    # Write a log entry
    with open(log_file, "a") as log:
        log.write(f"Image: {image_file} => PDF: {os.path.basename(pdf_path)}\n")

    with open(log_file, "a") as log:
        log.write("\nConversion Complete\n")