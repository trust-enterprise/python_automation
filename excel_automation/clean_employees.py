from openpyxl import load_workbook, Workbook

workbook = load_workbook("employees.xlsx")
sheet = workbook.active

total_records = 0
valid_records = 0
invalid_records = 0

seen_names = set()

new_workbook = Workbook()
new_sheet = new_workbook.active
new_sheet.append(["Name", "Age", "Department"])

for row in sheet.iter_rows(min_row=2, values_only=True):
    total_records += 1

    name = row[0].strip()
    age = row[1]
    department = row[2]

    if age is None:
        print(f"Missing age for: {name}")
        invalid_records += 1
        continue

    if name in seen_names:
        print(f"Duplicate employee: {name}")
        invalid_records += 1
        continue

    seen_names.add(name)

    print(f"Name: {name}, Age: {age}, Department: {department}")
    new_sheet.append([name, age, department])
    valid_records += 1

print(f"Valid records: {valid_records}")
print(f"Invalid records: {invalid_records}")
print(f"Total records: {total_records}")    

new_workbook.save("cleaned_employees.xlsx")