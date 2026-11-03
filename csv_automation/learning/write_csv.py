import csv

students = [
    ["Rahul", 22, "Lucknow"],
    ["Amit", 25, "Delhi"],
    ["Priya", 21, "Mau"]
]

with open("new_students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])

    #for student in students:
    #    writer.writerow(student)

    writer.writerow(["Suresh", 26, "Kanpur"])