import csv

def is_csv_file(filename):
    return filename.lower().endswith(".csv")

def is_valid_age(age):
    return age >= 0

filename = input("Enter CSV filename: ").strip()
if not is_csv_file(filename):
    print("Please enter a CSV file.")
    exit()

output_filename = input("Enter output CSV filename: ").strip()
if not is_csv_file(output_filename):
    print("Output filename must end with .csv")
    exit()

try:
    minimum_age = int(input("Enter minimum age: "))
except ValueError:
    print("Please enter a valid number.")
    exit()
if not is_valid_age(minimum_age):
    print("Age cannot be negative.")
    exit()


try:
    with open(filename, "r") as input_file:
        with open(output_filename, "x", newline="") as output_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(
                output_file,
                fieldnames=["name", "age", "city"]
            )
            
            writer.writeheader()

            seen_names = set()
            total_records = 0
            valid_records = 0
            invalid_records = 0
            written_records = 0

            for row in reader:
                total_records += 1

                row["name"] = row["name"].strip()

                try:
                    age = int(row["age"])
                except ValueError:
                    invalid_records += 1
                    print(f"Skipping invalid age for: {row['name']}")
                    continue
                
                if not is_valid_age(age):
                    invalid_records += 1
                    print(f"Skipping negative age for: {row['name']}")
                    continue

                valid_records += 1

                if not row["name"]:
                    print("Skipping record with missing name")
                    invalid_records += 1
                    continue

                if age >= minimum_age and row["name"] not in seen_names:
                    writer.writerow(row)
                    written_records += 1
                    seen_names.add(row["name"])

            print("\n--- Processing Summary ---")
            print(f"Total records: {total_records}")
            print(f"Valid records: {valid_records}")
            print(f"Invalid records: {invalid_records}")
            print(f"Records written: {written_records}")

except FileNotFoundError:
    print(f"Input file not found: {filename}")

except FileExistsError:
    print(f"Output file already exists: {output_filename}")