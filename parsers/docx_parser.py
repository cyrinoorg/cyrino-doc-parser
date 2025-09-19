from docx import Document

def parse_docx(file_path):
    """Parse text from a DOCX file."""
    doc = Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Example usage
# print(parse_docx('example.docx'))