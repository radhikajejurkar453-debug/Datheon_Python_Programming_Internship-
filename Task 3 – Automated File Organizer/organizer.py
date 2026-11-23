
import os
import shutil
import logging
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_FOLDER = SCRIPT_PATH.parent
LOG_FILE = PROJECT_FOLDER / "organizer.log"

PROJECT_FOLDER.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js", ".sql"],
    "Others": []
}


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    if not destination.exists():
        return destination

    parent = destination.parent
    name = destination.stem
    extension = destination.suffix
    counter = 1

    while True:
        new_destination = parent / f"{name}_{counter}{extension}"

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists():
        print("\nError: The specified folder does not exist.")
        logging.error("Folder does not exist: %s", folder)
        return

    if not folder.is_dir():
        print("\nError: The specified path is not a folder.")
        logging.error("Path is not a directory: %s", folder)
        return

    moved_files = 0
    skipped_files = 0
    error_files = 0

    print("\nStarting file organization...\n")
    logging.info("Organization started: %s", folder)

    try:
        with os.scandir(folder) as entries:
            for entry in entries:
                source = Path(entry.path)

                if not entry.is_file(follow_symlinks=False):
                    continue

                try:
                    category = get_category(source)
                    category_folder = folder / category

                    category_folder.mkdir(exist_ok=True)

                    destination = get_unique_destination(
                        category_folder / source.name
                    )

                    shutil.move(str(source), str(destination))

                    moved_files += 1

                    print(f"Moved: {source.name} -> {category}/")
                    logging.info(
                        "Moved %s to %s",
                        source.name,
                        destination
                    )

                except PermissionError as error:
                    error_files += 1
                    print(f"Permission denied: {source.name}")
                    logging.error("Permission error for %s: %s", source, error)

                except FileNotFoundError as error:
                    error_files += 1
                    print(f"File not found: {source.name}")
                    logging.error("File not found: %s", error)

                except (shutil.Error, OSError) as error:
                    error_files += 1
                    print(f"Could not move {source.name}: {error}")
                    logging.error("Could not move %s: %s", source, error)

    except PermissionError as error:
        print(f"Cannot access folder: {error}")
        logging.error("Cannot access folder %s: %s", folder, error)
        return

    logging.info(
        "Organization completed. Moved: %d, Skipped: %d, Errors: %d",
        moved_files,
        skipped_files,
        error_files
    )

    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Folder: {folder}")
    print(f"Files moved: {moved_files}")
    print(f"Files skipped: {skipped_files}")
    print(f"Errors: {error_files}")
    print("==========================================")
    print(f"\nLog file saved at: {LOG_FILE}")


def main():
    print("===================================")
    print("     AUTOMATED FILE ORGANIZER")
    print("===================================")

    folder_path = input(
        "\nEnter the folder path to organize:\n"
    ).strip().strip('"')

    organize_files(folder_path)


if __name__ == "__main__":
    main()

