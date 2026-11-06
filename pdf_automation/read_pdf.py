from pypdf import PdfReader

reader = PdfReader("employees.pdf")

for page in reader.pages:
    text = page.extract_text()
    print(text)