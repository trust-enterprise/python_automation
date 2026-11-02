from datetime import datetime
from pathlib import Path
import shutil

folder = Path(input("Enter folder path: "))
log_path = folder / "activity.log"

# Track file processing results
moved_count = 0
failed_count = 0
skipped_count = 0

# Check whether the source folder exists
if not folder.is_dir():
    print("Invalid folder path:", folder) 
else:
    total_files = sum(1 for file in folder.iterdir() if file.is_file()  and file != log_path)
    print("Total files found:", total_files)
    
    if total_files == 0:
        print("No files to organize.")
    else:
        while True:
            choice = input("Preview only? (y/n): ").strip().lower()

            if choice in ("y", "n"):
                break

            print("Invalid choice. Enter y or n.")

        dry_run = choice == "y"

        if dry_run:
            for file in folder.iterdir():
                if file.is_file() and file != log_path:
                    extension = file.suffix.lower().replace(".", "")

                    if extension:
                        destination = folder / extension
                    else:
                        destination = folder/'others'
                    
                    target = destination / file.name

                    if not target.exists(): 
                        print(f"Would move: {file.name} -> {target}\n")
                    else:
                        print("File already exists:", file.name)   
            print("Preview completed. No files were moved.") 
        else:
            with open(log_path, "a") as log_file:
                for file in folder.iterdir():
                    if file.is_file() and file != log_path:
                        extension = file.suffix.lower().replace(".", "")

                        if extension:
                            destination = folder / extension
                        else:
                            destination = folder/'others'
                        
                        target = destination / file.name

                        if not target.exists(): 
                            try:
                                destination.mkdir(exist_ok=True)
                                shutil.move(str(file), str(target))
                                moved_count += 1
                                log_file.write(f"{datetime.now()} - Moved: {file.name}\n")
                            except PermissionError:
                                failed_count += 1
                                print("Permission denied:", file.name)
                                log_file.write(f"{datetime.now()} - Permission denied: {file.name}\n")
                            except FileNotFoundError:
                                failed_count += 1
                                print("File not found:", file.name)
                                log_file.write(
                                    f"{datetime.now()} - File not found: {file.name}\n"
                                )
                            except OSError as error:
                                failed_count += 1
                                print("File system error:", error)
                                log_file.write(
                                    f"{datetime.now()} - File system error: {file.name} - {error}\n"
                                )
                                
                        else:
                            print("File already exists:", file.name)
                            skipped_count += 1
                            log_file.write(f"{datetime.now()} - Skipped: {file.name}\n")
                
                print("Files moved:", moved_count)
                print("Files failed:", failed_count)
                print("Files skipped:", skipped_count)

                if total_files > 0:
                    success_rate = (moved_count / total_files) * 100 
                print(f"Success rate: {success_rate:.2f}%")

                if failed_count == 0:
                    print("Processing completed without errors!")
                else:
                    print("Completed with some errors.")