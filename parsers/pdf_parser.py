import PyPDF2

def parse_pdf(file_path):
    """Parse text from a PDF file."""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Example usage
# print(parse_pdf('example.pdf'))