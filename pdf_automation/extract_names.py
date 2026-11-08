from pypdf import PdfReader

reader = PdfReader("employees.pdf")

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
            employee["Age"] = line.split(":", 1)[1].strip()

        elif line.startswith("Department:"):
            employee["Department"] = line.split(":", 1)[1].strip()

if employee:
    employees.append(employee)

print(employees)