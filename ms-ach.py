import openpyxl
from xml.etree import ElementTree as ET
from xml.dom import minidom

# Load Excel data
excel_file_path = 'data.xlsx'  # Change this to the path of your Excel file
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

# Initialize XML structure
xml_root = ET.Element('Localization', xmlns="http://config.mgt.xboxlive.com/schema/localization/1")

# Define locales
locales = ["en-US", "fr-FR", "ja-JP", "ru-RU", "es-ES", "zh-CN", "de-DE", "pl-PL"]

# Iterate over rows in the Excel sheet and create XML structure
for row in sheet.iter_rows(min_row=2):  # Assuming data starts from the second row
    for i, locale in enumerate(locales):
        if i + 1 < len(row):  # Check if the next column exists
            value_elem = ET.SubElement(xml_root, 'Value', locale=locale)
            value_elem.text = str(row[i + 1].value) if row[i + 1].value is not None else ''

    # Add 5 empty lines after each row
    for _ in range(5):
        ET.SubElement(xml_root, 'EmptyLine')

# Create a formatted XML string
xml_string = ET.tostring(xml_root, encoding='utf-8').decode('utf-8')
formatted_xml = minidom.parseString(xml_string).toprettyxml(indent='\t')

# Save the XML to a file
with open('output.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(formatted_xml)

print('XML document successfully created and saved to output.xml.')
