from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json, convert_to_dict
import csv
from bs4 import BeautifulSoup
import os

filename = os.path.join(".", "ocr.pdf")
output_filename = os.path.join(".", "outputs.json")

elements = partition_pdf(filename=filename, infer_table_structure=True)
elements_to_json(elements, filename=output_filename)
tables = [el for el in elements if el.category == "Table"]
# with open("example-10k.html", "rb") as f:
#     elements = partition(file=f)
# Function to extract data from HTML table
def extract_data_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    return data

# Function to write data to CSV
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Insurer", "Procedure/Service", "Procedure/Service Description", "Original Effective Date", "Revised", "Procedure CPT/HCPCS Code", "Prior authorization"])
        for item in data:
            writer.writerow(item)



# Extracting and processing data
data = []
for table in tables:
    html_content = table.metadata.text_as_html
    # Save the HTML content to a file
    with open("temp.html", "w") as file:
        file.write(html_content)
    table_data = extract_data_from_html(html_content)
    for row in table_data[1:]:  # Skipping header row
        if len(row) > 1:
            procedure = row[0]
            try:
                codes = row[2]
                # Continue processing with 'codes' variable
            except IndexError:
                # For example, you can assign a default value to 'codes' or skip processing
                codes = ''  # Or any other default value you prefer
                pass
            prior_auth = row[1]
            data.append(["Ohio Medicaid", procedure, "", "Jan. 1, 2024", "", codes, prior_auth])


# Writing data to CSV
write_to_csv(data, 'insurance_data.csv')
