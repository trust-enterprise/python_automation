import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader: 
        name = row[0]
        age = row[1]
        city = row[2]

        if int(age) > 22: 
            print(f"{name} is {age} years old and lives in {city}.")