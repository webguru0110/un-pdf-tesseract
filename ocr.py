import pytesseract
from PIL import Image

import os

image_path = os.path.join(".", "ocr.jpg")
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)
with open("output.txt", "w") as output_file:
    output_file.write(extracted_text)
