# File Organizer

A simple Python project that automatically organizes mixed files into separate folders based on their file extensions.

## What It Does

This program takes a folder containing different types of files and organizes them into six categories:

- **Images**
- **Documents**
- **Videos**
- **Audio**
- **Archives**
- **Other**

It checks each file's extension and moves the file into the appropriate category folder. If a file has an extension that is not included in the program's category dictionary, it moves that file into the `Other` folder.

## A Promise It Keeps

The program prevents files from being overwritten when two files have the same name.

If a file with the same name already exists in the destination folder, the program generates a new available filename.

For example:

- `a.jpg`
- `a_1.jpg`
- `a_2.jpg`

This helps prevent filename conflicts.

## Requirements

- Python 3
- No external packages required.
- `pathlib` and `shutil` are included in Python's standard library.

## How to Run It

**Step 1:** Clone or download this repository.

**Step 2:** Open the `file-organizer` project folder in VS Code.

**Step 3:** Make sure the `sample_files` folder is next to `main.py`.

**Step 4:** Open the VS Code terminal:

`Terminal → New Terminal`

**Step 5:** Run the program using:

```powershell
python main.py
```

## Example Output

```text
Moved a.jpg to sample_files\Images\a_1.jpg
Moved c.pdf to sample_files\Documents\c_1.pdf
```

*Your actual output depends on the files in the source folder.*

## What I Learned

### 1. Understanding `list(folder.iterdir())`

At first, I thought `list()` would simply display all the filenames inside my folder. However, when I used `list(folder.iterdir())`, I learned that it collects the folder contents as a Python list of `Path` objects. These objects represent file or folder paths, rather than just bare filenames.

I also learned that creating this list before the loop gives me a snapshot of the original folder contents. This helps me iterate over the original items safely while moving files and changing the folder contents.

### 2. Understanding the Counter Variable

I initially tried to use one `counter` variable for two different purposes. However, I discovered that resetting its value for each new file prevented it from keeping a total count of all moved files.

I learned that separate variables should be used when they have separate responsibilities.

### 3. Learning How Files Move

I learned how `shutil.move()` moves a file from its original location to a destination folder. I also practiced using `item.is_file()` to check whether an item is a file rather than a folder.

### 4. Testing Multiple Files

In my `x.txt` and `y.txt` experiment, I expected the program to process both files. Both files were included in the folder iteration, and I used the experiment to understand how the program handles multiple files. This helped me understand why collecting the folder contents before the loop is useful when files are being moved.

## Warning

This program **moves files; it does not copy them**. After running it, the original files are located inside their category folders rather than in their original source location.

Running the program again will not organize those same files a second time because they have already been moved. Keep a backup of important files before testing.

## Project Structure

```text
file-organizer/
│
├── main.py
├── README.md
└── sample_files/
    ├── a.jpg
    ├── b.png
    ├── c.pdf
    └── ...
```

## Future Improvements

- Add support for more file extensions.
- Improve error handling.
- Add a summary showing the total number of files moved.
- Allow users to select a source folder.
