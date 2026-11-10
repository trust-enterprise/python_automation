from PIL import Image
from pathlib import Path

folder = Path(r"C:\Users\dove\Music")

for file in folder.glob("*.webp"):
    image = Image.open(file)

    output_file = file.with_suffix(".jpg")

    image.convert("RGB").save(output_file)

    print(f"Converted: {file.name} -> {output_file.name}")

print("Conversion completed!")