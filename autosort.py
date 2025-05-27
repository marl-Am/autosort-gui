import os
import shutil
import argparse
from datetime import datetime

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [
        ".pdf",
        ".docx",
        ".doc",
        ".txt",
        ".xlsx",
        ".xls",
        ".pptx",
        ".ppt",
        ".csv",
    ],
    "Code": [
        ".py",
        ".js",
        ".html",
        ".css",
        ".java",
        ".c",
        ".cpp",
        ".ts",
        ".json",
        ".xml",
        ".sh",
        ".bat",
        ".md",
    ],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    filename_lower = filename.lower()
    if filename_lower == ".gitignore":
        return "Code"
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder
    return "Others"


def sort_by_type(directory):
    moved = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            folder = get_file_type(item)
            dest_folder = os.path.join(directory, folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_folder, item))
            moved.append(f"{item} → {folder}")
    return moved


def sort_by_date(directory):
    moved = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            mod_time = os.path.getmtime(item_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m")
            dest_folder = os.path.join(directory, date_folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_folder, item))
            moved.append(f"{item} → {date_folder}")
    return moved


def main():
    parser = argparse.ArgumentParser(
        description="AutoSort: Automatically sort files by type or date."
    )
    parser.add_argument("directory", help="Target directory to sort")
    parser.add_argument(
        "--mode",
        choices=["type", "date"],
        default="type",
        help="Sorting mode: 'type' or 'date'",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("❌ Invalid directory.")
        return

    if args.mode == "type":
        results = sort_by_type(args.directory)
    else:
        results = sort_by_date(args.directory)

    print(f"\n✅ Sorted {len(results)} file(s):")
    for line in results:
        print(" -", line)


if __name__ == "__main__":
    main()
