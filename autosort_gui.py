import os
import shutil
import tkinter as tk
from tkinter import filedialog
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

    # Explicitly handle filenames without extensions
    if filename_lower == ".gitignore":
        return "Code"

    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder

    return "Others"


def sort_by_type(target_dir):
    moved = []
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isfile(item_path):
            folder = get_file_type(item)
            print(f"Processing '{item}' → Detected type: '{folder}'")  # Debug print
            dest_folder = os.path.join(target_dir, folder)
            os.makedirs(dest_folder, exist_ok=True)
            try:
                shutil.move(item_path, os.path.join(dest_folder, item))
                moved.append(f"{item} → {folder}")
            except Exception as e:
                print(f"Error moving {item}: {e}")
    return moved


def sort_by_date(target_dir):
    moved = []
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isfile(item_path):
            mod_time = os.path.getmtime(item_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m")
            dest_folder = os.path.join(target_dir, date_folder)
            os.makedirs(dest_folder, exist_ok=True)
            try:
                shutil.move(item_path, os.path.join(dest_folder, item))
                moved.append(f"{item} → {date_folder}")
            except Exception as e:
                print(f"Error moving {item}: {e}")
    return moved


def run_sort():
    path = path_var.get()
    mode = mode_var.get()
    if not os.path.isdir(path):
        status_var.set("Invalid directory.")
        return
    try:
        if mode == "Type":
            result = sort_by_type(path)
        elif mode == "Date":
            result = sort_by_date(path)

        if result:
            details = "\n".join(result[-3:])  # Show last 3 entries
        else:
            details = "No files moved."

        time_now = datetime.now().strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
        status_var.set(f"Sorted {len(result)} file(s).\n{details}\nDone at {time_now}.")
    except Exception as e:
        print(f"Error: {e}")
        status_var.set(f"Error: {e}")


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_var.set(folder)


# GUI Setup
app = tk.Tk()
app.title("AutoSort GUI")
app.geometry("400x300")

path_var = tk.StringVar()
mode_var = tk.StringVar(value="Type")
status_var = tk.StringVar(value="Ready")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Select Folder:").pack(anchor="w")
tk.Entry(frame, textvariable=path_var, width=40).pack(side="left", padx=(0, 10))
tk.Button(frame, text="Browse", command=browse_folder).pack(side="left")

frame2 = tk.Frame(app, pady=10)
frame2.pack(fill="x")
tk.Label(frame2, text="Sorting Mode:").pack(anchor="w")
tk.OptionMenu(frame2, mode_var, "Type", "Date").pack(fill="x")

tk.Button(app, text="Run Sort", command=run_sort, bg="green", fg="white").pack(pady=10)

status_bar = tk.Label(
    app,
    textvariable=status_var,
    bd=1,
    relief="sunken",
    anchor="w",
    justify="left",
    wraplength=380,
)
status_bar.pack(side="bottom", fill="x", padx=5, pady=5)

app.mainloop()
