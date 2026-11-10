# PROJECT FEATURES:
# PDF file handling.
# Extracting employee records from PDFs.
# Employee information validation.
# Skipping incomplete and invalid records.
# Duplicate record detection and removal.
# Saving valid records into CSV files.
# Tracking duplicate counts.

from pypdf import PdfReader
import csv
from pathlib import Path

def is_valid_csv(filename):
    return filename.lower().endswith(".csv")

def is_valid_age(age):
    return age is not None and age > 0

pdf_path = Path("employees.pdf")

if not pdf_path.exists():
    print("Error: PDF file not found!")
    raise SystemExit

try:
    reader = PdfReader(pdf_path)

    if reader.is_encrypted:
        print("Error: PDF is password protected!")
        raise SystemExit

except Exception as e:
    print(f"Error: Unable to read PDF file: {e}")
    raise SystemExit

employees = []
employee = {}

for page in reader.pages:
    text = page.extract_text()

    for line in text.splitlines():

        if line.startswith("Name:"):

            if employee:
                employees.append(employee)

            employee = {}
            employee["Name"] = line.split(":", 1)[1].strip()

        elif line.startswith("Age:"):
            try:
                employee["Age"] = int(line.split(":", 1)[1].strip())
            except ValueError:
                employee["Age"] = None

        elif line.startswith("Department:"):
            employee["Department"] = line.split(":", 1)[1].strip()

if employee:
    employees.append(employee)

print("\nAll employees", employees)

valid_records = 0
invalid_records = 0

for employee in employees:

    if (
        not employee.get("Name")
        or not is_valid_age(employee.get("Age"))
        or not employee.get("Department")
    ):
        invalid_records += 1
        print("Incomplete record:", employee)

    else:
        valid_records += 1
        print("Valid record:", employee)

written_records = 0

output_csv_name = input("Enter output CSV filename: ").strip()

if not is_valid_csv(output_csv_name):
    print("Error: Filename must end with .csv")
    raise SystemExit

csv_path = Path(output_csv_name)

if csv_path.exists():
    print("Error: Output CSV already exists!")
    raise SystemExit 

seen_employees = set()
duplicate_records = 0

with open(csv_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Age", "Department"]
    )

    writer.writeheader()

    for employee in employees:

        if (
            employee.get("Name")
            and employee.get("Age") is not None
            and employee.get("Department")
        ):
            record = (
                employee["Name"],
                employee["Age"],
                employee["Department"]
            )

            if record in seen_employees:
                duplicate_records += 1
                continue
            
            seen_employees.add(record)

            writer.writerow(employee)
            written_records += 1

print("Valid employee records saved to CSV!")

print("\n--- Processing Summary ---")
print("Total employee records:", len(employees))
print("Valid records:", valid_records)
print("Invalid records:", invalid_records)
print("Duplicate records:", duplicate_records)
print("Records saved to CSV:", written_records,"\n")