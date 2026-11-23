# Automated File Organizer

A Python-based utility that automatically organizes files into separate folders based on their file extensions. It helps keep directories clean and structured while handling duplicate filenames and recording file operations through logging.

## Project Overview

The Automated File Organizer is developed using Python's built-in libraries. It scans a selected directory, identifies files based on their extensions, creates appropriate category folders, and moves files into those folders.

## Features

- **Automatic File Categorization:** Organizes files based on their extensions.
- **Folder Creation:** Automatically creates category folders when required.
- **Duplicate File Handling:** Prevents overwriting by generating unique filenames.
- **Error Handling:** Handles permission errors and file movement errors.
- **Logging:** Records file operations, errors, and execution details.
- **Execution Summary:** Displays the number of files moved, skipped, and errors encountered.

## Technologies Used

- Python 3
- os
- shutil
- logging
- pathlib

## Project Structure

```text
Automated-File-Organizer/
│
├── organizer.py
├── README.md
├── .gitignore
├── organizer.log
└── Test_Files/
    ├── sample.txt
    ├── photo.png
    ├── data.zip
    ├── program.py
    └── video.mp4
```

*The sample test files are used to demonstrate file organization.*

## File Categories

| Category | Supported Extensions |
|---|---|
| Documents | PDF, DOCX, TXT, PPTX, XLSX, CSV |
| Images | JPG, PNG, GIF, BMP, SVG, WEBP |
| Videos | MP4, MKV, MOV, AVI |
| Audio | MP3, WAV, AAC, FLAC |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JAVA, CPP, C, HTML, CSS, JS, SQL |
| Others | Other file extensions |

## Requirements

- Python 3.x
- No external Python packages required.

## How to Run

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Automated-File-Organizer.git
```

**Step 2: Open the project directory**

```bash
cd Automated-File-Organizer
```

**Step 3: Run the Python program**

```bash
python organizer.py
```

**Step 4: Enter the folder path**

When prompted, enter the directory you want to organize.

Example:

```text
C:\Task_3_File_Organizer\Test_Files
```

The program will automatically organize the files into their respective category folders.

## Testing Results

The program was tested using six sample files.

| Test File | Category | Result |
|---|---|---|
| data.zip | Archives | Successful |
| notes.txt | Documents | Successful |
| photo.png | Images | Successful |
| program.py | Code | Successful |
| resume.pdf | Documents | Successful |
| video.mp4 | Videos | Successful |

**Execution Summary:**
- Files moved: 6
- Files skipped: 0
- Errors: 0

## Logging

The application generates an `organizer.log` file to record:

- Organization start and completion.
- Successfully moved files.
- File movement errors.
- Execution summary.

## Learning Outcomes

Through this project, I practised:

- Python file handling.
- Working with directories and file extensions.
- Using built-in Python libraries.
- Exception handling.
- Logging and debugging.
- Automating repetitive file management tasks.

## Author

**Radhika Jejurkar**  
B.Sc. Data Science Student

## Project

Automated File Organizer – Python Programming Internship Task 3
