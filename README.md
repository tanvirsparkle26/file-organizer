# File Organizer

## What it does 
This program takes a folder full of mixed files and makes them into six categories folder Such as Documents, Images, Videos, Audio, Archives and Other. It takes unorganized files from the folder and moved them into their own categories/ sub folder. If a file has different extentions are appears outside of the dictionary then it moves to 'Other' folder. 

## A promise it keeps
If two files have the same name ,which one already exists in the destination folder. Then the program will create a new free file name for that files to avoid clash. Such as 'a.jpg becomes a_1.jpg' .
 
## How to run it

**Requirements**
- Python 3 (check with: `python --version`)
- No extra packages needed. `pathlib` and `shutil` come with Python.

**Steps**
1. Put the `sample_files` folder next to `main.py`, inside the `file-organizer` folder.
2. Open VS Code (or any terminal).
3. Click **File → Open Folder**, then select the `file-organizer` folder.
4. Click **Terminal → New Terminal**. A terminal opens at the bottom, already inside the folder.
5. Type this command and press Enter: python main.py

## Example Output 
moved a.jpg to sample_files\Images\a_1.jpg
moved c.pdf to sample_files\Documents\c_1.pdf

## What I learned
I thought list() might simply display all the files inside my folder.When I used list(folder.iterdir()), it collected the paths of all the items inside my folder into a Python list, such as a.jpg, c.pdf, and g.mp3 .This list gives my for loop a snapshot of the original folder items to process, protecting my iteration from problems caused by moving files and changing the folder's contents during the loop.
I have  used and tried one variable for doing two jobs . But it gives some silent errors. I used counter variable for doing two jobs in this program, but it cannot count how many files are moved because its wiped out the value of counter for every new files. 
I also learned how shutil.move() moves a file to its destination folder. First , i learned how to check whether a item is file or  folder with if item.is_file():