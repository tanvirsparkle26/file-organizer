from pathlib import Path
import shutil
import sys

folder = Path("sample_files")

if not folder.exists():
    print("sample_files not found. Create a folder named sample_files next to main.py, put some files inside it, then run again.")
    sys.exit()


categories = {
    ".pdf" : "Documents",
    ".jpg" : "Images",
    ".mp4" : "Videos",
    ".png" : "Images",
    ".txt" : "Documents",
    ".docx" : "Documents",
    ".zip" : "Archives",
    ".mp3" : "Audio",
    ".jpeg" : "Images",
    ".rar" : "Archives",
}

for new_item in categories.values():
    (folder / new_item).mkdir(exist_ok=True)

(folder / "Other").mkdir(exist_ok=True)
counter = 0    
for item in list(folder.iterdir()):
    if item.is_file():
        ending = item.suffix.lower()
        category = categories.get(ending, "Other")
        destination = folder / category / item.name
        duplicate_number = 1
        while destination.exists():
            new_name = f"{item.stem}_{duplicate_number}{item.suffix}"
            destination = folder / category / new_name
            duplicate_number += 1
        shutil.move(item, destination)
        counter += 1
        print(f"moved {item.name} to {destination}")
if counter == 0:
    print("No files were moved. There are no files directly in the sample_files. Put some files inside the sample_files, then run again.")
      
