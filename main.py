import pdfplumber
import re
import json


def extract_fields_from_pdf_text(text):
    """
    Extracts key financial fields such as Gross Salary, Net Salary, Income from Other Sources,
    Income chargeable under Salaries, and Total Tax Deducted from the provided text.
    
    Args:
        text (str): The full text extracted from the PDF.
    
    Returns:
        dict: A dictionary with keys 'Gross Salary', 'Net Salary', 'Income from Other Sources',
              'Income chargeable under Salaries', and 'Total Tax Deducted', with their corresponding
              numeric values extracted from the text or None if the value was not found.
    """

    extracted_data = {
        "Gross Salary": None,
        "Net Salary": None,
        "Income from Other Sources": None,
        "Income chargeable under Salaries": None,
        "Total Tax Deducted": None
    }

    lines = text.replace(",", "").lower().split("\n")

    for i, line in enumerate(lines):
        if "gross salary" in line:
            extracted_data["Gross Salary"] = find_numeric_value_in_line(line)
        elif "net salary" in line:
            extracted_data["Net Salary"] = find_numeric_value_in_line(line)
        elif "income from other sources" in line:
            extracted_data["Income from Other Sources"] = find_numeric_value_in_line(line)
        elif "Income chargeable under the head ‘Salaries’" in line:
            extracted_data["Income chargeable under Salaries"] = find_numeric_value_in_line(line)
        elif "total tax deducted" in line or "total tax" in line:
            extracted_data["Total Tax Deducted"] = find_numeric_value_in_line(line)

    return extracted_data


def find_numeric_value_in_line(line):
    """
    Finds and extracts the first numeric value from a given line of text using a regular expression.
    
    Args:
        line (str): A line of text where the numeric value will be searched for.
    
    Returns:
        str: The first numeric value found in the line, with spaces removed, or None if no match is found.
    """

    match = re.search(r"(\d+[\d\s]*\d+)", line)
    if match:
        return match.group(1).strip()
    return None

# Extract text from all pages of the PDF
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from all pages of a PDF document using the pdfplumber library.
    
    Args:
        pdf_path (str): The file path to the PDF document.
    
    Returns:
        str: The complete extracted text from the entire PDF.
    """

    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
    return full_text


def save_to_json(data, file_path):
    """
    Saves the extracted data to a JSON file.
    
    Args:
        data (dict): The dictionary containing extracted data.
        file_path (str): The path where the JSON file will be saved.
    """
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


pdf_path = 'sampleitr.pdf'

pdf_text = extract_text_from_pdf(pdf_path)

extracted_data = extract_fields_from_pdf_text(pdf_text)

json_file_path = 'extracted_data.json'
save_to_json(extracted_data, json_file_path)

print(f"Extracted data has been saved to {json_file_path}")