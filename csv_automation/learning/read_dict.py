import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # print(f"{row['name']} lives in {row['city']}.")
        if row["city"] == "Delhi":
            print(row["name"])