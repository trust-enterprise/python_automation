# PROJECT FEATURES:
# Excel file handling.
# Reading and writing Excel workbooks.
# Worksheet and cell operations.
# Input and filename validation.
# Data cleaning and filtering.
# Duplicate record detection.
# Missing and invalid data validation.
# Reusable validation functions.
# Exception handling.
# Processing counters and summary reports.

from openpyxl import load_workbook, Workbook 

try:
    workbook = load_workbook("employees.xlsx")
except FileNotFoundError:
    print("Input Excel file not found.")
    exit()
except Exception as e:
    print(f"Unable to read Excel file: {e}")
    exit()

sheet = workbook.active

total_records = 0
valid_records = 0
invalid_records = 0
written_records = 0

seen_records = set()

new_workbook = Workbook()
new_sheet = new_workbook.active
new_sheet.append(["Name", "Age", "Department"])

try:
    minimum_age = int(input("Enter minimum age: "))

    if minimum_age < 0:
        print("Age cannot be negative.")
        exit()

except ValueError:
    print("Please enter a valid number.")
    exit()

def is_valid_department(department):
    return department is not None and department.strip() != ""

def is_valid_name(name):
    return name is not None and name.strip() != ""

def is_valid_age(age):
    return age is not None and age >= 0

for row in sheet.iter_rows(min_row=2, values_only=True):
    total_records += 1

    name = row[0] 
    age = row[1]
    department = row[2]  

    if name is not None:
        name = name.strip()
    if not is_valid_name(name):
        print("Missing employee name in this recod")
        invalid_records += 1
        continue

    if not is_valid_age(age):
        print(f"Invalid age for: {name}")
        invalid_records += 1
        continue

    if department is not None:
        department = department.strip()
    if not is_valid_department(department):
        print(f"Missing department for: {name}")
        invalid_records += 1
        continue


    record = (name, age, department)

    if record in seen_records:
        print("Duplicate record")
        invalid_records += 1
        continue

    seen_records.add(record)

    print(f"Name: {name}, Age: {age}, Department: {department}")
    if age >= minimum_age:
        new_sheet.append([name, age, department])
        written_records += 1
    valid_records += 1

print(f"Records written: {written_records}")
print(f"Valid records: {valid_records}")
print(f"Invalid records: {invalid_records}")
print(f"Total records: {total_records}")    

output_filename = input("Enter output filename: ").strip()
if not output_filename.lower().endswith(".xlsx"):
    print("Please enter an Excel filename ending with .xlsx")
    exit()
try:
    new_workbook.save(output_filename)
except PermissionError:
    print("Please close the output Excel file and try again.")