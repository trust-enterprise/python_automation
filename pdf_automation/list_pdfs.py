from pathlib import Path
from pypdf import PdfReader

input_folder = Path("input_pdfs")

pdf_files = list(input_folder.glob("*.pdf"))

processed_files = 0

for pdf_path in pdf_files:
    print(f"\nProcessing: {pdf_path.name}")

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        text = page.extract_text()
        print(text) 

    processed_files += 1

print("\nTotal PDFs processed:", processed_files)