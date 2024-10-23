import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import pandas as pd
import os

# Define the path to the PDF file
pdf_path = os.path.join(".", "4.8.24 TOPS (Black bins) manicure batch.pdf")

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Create a list to hold the extracted text
extracted_text_list = []

# Iterate through each page
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    pix = page.get_pixmap()

    # Save the image of the page to a temporary file
    image_path = f'page_{page_num}.png'
    pix.save(image_path)

    # Open the image and apply OCR
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    extracted_text_list.append(extracted_text)

    # Remove the temporary image file
    os.remove(image_path)

# Join the extracted text into a single string
extracted_text = "\n".join(extracted_text_list)

# Save the extracted text to a text file (optional)
with open('output.txt', 'w') as output_file:
    output_file.write(extracted_text)

# Parse the extracted text and convert to a DataFrame
# This part will vary based on the structure of the extracted text
# Here we assume a simple parsing strategy

rows = []
for line in extracted_text.split('\n'):
    if line.strip():
        rows.append(line.split())

# Convert list of rows into a DataFrame
df = pd.DataFrame(rows)

# Save the DataFrame to an Excel file
df.to_excel('4.8.24 TOPS (Black bins) manicure batch.xlsx', index=False)

print("PDF content successfully extracted and saved to pdf_excel.xlsx")
