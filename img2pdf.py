

import img2pdf
import os

with open("imagetopdf.pdf","wb") as file:

    file.write(img2pdf.convert([i for i in os.listdir("C:\\vaishak\\images")]))