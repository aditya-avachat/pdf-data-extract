# PDF Data Extraction Script

This repository demonstrates how to extract specific data fields from a PDF file (non-scanned) using **pdfplumber** and **regular expressions**. The script focuses on extracting the following financial fields from the PDF:

- Gross Salary
- Net Salary
- Income from Other Sources
- Income Chargeable under Salaries
- Total Tax Deducted

## Approach Overview

The extraction approach relies on:

1. **Text Extraction**: We use the `pdfplumber` library to extract the text from the PDF.
2. **Pattern Matching**: Once the text is extracted, we apply **regular expressions** to match specific patterns (e.g., "Gross Salary", followed by a numeric value).
3. **Field Mapping**: We identify key fields based on proximity in the extracted text and then extract the associated numeric values.

## Execution Instructions

### Prerequisites

Ensure you have the following Python packages installed:

- `pdfplumber`
- `re`
- `json`

You can install the required dependencies by running:

```bash
pip install pdfplumber
```


### Running the Code

1. **Place your PDF file** in the same directory as the script and make sure the filename is correctly set in the code (e.g., `'sampleitr.pdf'`).
2. **Run the script** :
   ```
   python main.py
   ```
3. **Check the Output** : The script will extract the required fields from the PDF and save the results as a JSON file (`extracted_data.json`). A confirmation 					  message will be printed to the console.



## Thought Process and Challenges

### Current Approach

* **Text-Based Extraction** : We use **pdfplumber** to extract text from a structured PDF. The text is then split into lines, and **regular expressions** are used to search for specific fields based on keywords and patterns.
* **Pattern Matching** : This method assumes that the text surrounding key fields like "Gross Salary" or "Net Salary" will be predictable, making it possible to extract the numerical value that appears after each keyword.

### Challenges Faced

1. **Unstructured Text** : Although the PDF is not scanned, the extracted text may not always have a clear structure. Fields can appear in different formats or locations, making it difficult to apply a consistent rule for extracting values.
2. **Non-Robustness** : Regular expressions work for specific formats, but any change in the structure of the document can break the extraction process. For example, if a field appears on a different line or if the format of the numbers changes (e.g., with additional symbols or spaces), the script may fail to capture the values correctly.
3. **Manual Adjustments** : Since this approach is heavily dependent on text structure, it is not easily scalable to different types of PDFs or forms. Each new document might require new regular expressions or manual tweaking.

### Limitations of Current Approach

* **Inflexibility** : The current approach is **not scalable** because it relies on specific patterns and fixed locations for data. If the format of the PDF changes even slightly, the script may not extract the fields correctly.
* **Handling Edge Cases** : PDFs with different formatting or fields spread across multiple lines can lead to incorrect extraction or missing data.

## Why OCR + LLM Would Be More Robust

Using **OCR (Optical Character Recognition)** combined with a **Language Model (LLM)** would provide a more robust, scalable, and reliable solution for extracting data from PDFs, especially for scanned or complex documents.

### Advantages of OCR + LLM

1. **Handling Scanned PDFs** : OCR can extract text from scanned documents, something that current text extraction libraries like `pdfplumber` cannot handle. This is crucial if the documents are not machine-readable.
2. **Layout-Aware** : LLMs like **LayoutLM** can consider the layout and structure of the document, making it easier to extract fields even if they are in unpredictable locations.
3. **Contextual Understanding** : An LLM can understand the context and relationships between different fields, making it easier to extract values from unstructured or semi-structured documents.
4. **Scalability** : The combination of OCR and LLM can generalize across different types of documents and layouts without requiring manual tweaking of regular expressions. This would allow the solution to scale for different document formats without the need for constant adjustments.

### Possible Improvements

* **OCR Integration** : Incorporate OCR using a library like **Tesseract** to handle scanned PDFs. This would allow the script to work with a wider variety of documents.
* **LLM-Based Extraction** : Use a language model like **LayoutLM** (or a pre-built API like **Google Vision** or  **Amazon Textract** ) to extract key fields based on layout and contextual understanding, rather than relying on brittle pattern-matching methods.

## Conclusion

While the current approach using `pdfplumber` and regular expressions works for certain structured PDFs, it is **not scalable** or **reliable** for handling documents with varied formats. An approach leveraging **OCR** and **LLMs** would significantly improve accuracy, robustness, and scalability, allowing extraction from a wider range of documents and formats without manual intervention.
