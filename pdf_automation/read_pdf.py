# PROJECT FEATURES:
# PDF file handling using pypdf.
# Reading PDF pages.
# Extracting text from PDF.
# Saving extracted text into a .txt file.
# Page numbering using enumerate().
# Counting PDF pages using len().

from pypdf import PdfReader

reader = PdfReader("employees.pdf")

total_pages = len(reader.pages)
print(f"Total pages: {total_pages}")

with open("extracted_text.txt", "w", encoding="utf-8") as file:

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        file.write(f"--- Page {page_number} ---\n")
        file.write(text)
        file.write("\n\n")

print("PDF text saved successfully!")