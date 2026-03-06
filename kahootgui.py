import random
import string
import tkinter as tk
import logging
import zipfile
import platform
import os
import subprocess  # Added to open explorer/finder
from datetime import datetime

# --- Global Config & Filenames ---
log_filename = datetime.now().strftime("%I-%M-%S_%B-%d-%Y.log")
zip_filename = log_filename.replace(".log", ".zip")

# Custom logging factory to handle conditional OS info
old_factory = logging.getLogRecordFactory()
def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    if hasattr(root, 'os_logging_var') and root.os_logging_var.get():
        record.os_info = f"[{platform.system()} {platform.release()}] "
    else:
        record.os_info = ""
    return record

logging.setLogRecordFactory(record_factory)

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(os_info)sCODE: %(message)s',
    datefmt='%I:%M:%S %p'
)

# --- Functions ---

def open_folder():
    """Opens the directory where the logs are stored."""
    path = os.path.realpath(os.getcwd())
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # Linux
        subprocess.Popen(["xdg-open", path])

def zip_log():
    """Compresses the current log file into a zip."""
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as archive:
            archive.write(log_filename)
    except Exception as e:
        print(f"Zip failed: {e}")

def generate_code():
    rc_list = [random.choice(string.ascii_uppercase + string.digits) for _ in range(6)]
    new_code = "".join(rc_list)
    timestamp = datetime.now().strftime("%I:%M:%S %p")

    status_label.config(text=f"Last generated at: {timestamp}")
    result_label.config(text="Room Code: " + new_code)

    logging.info(new_code)

    if zip_var.get():
        zip_log()
        print(f"Logged & Zipped: {new_code}")
    else:
        print(f"Logged: {new_code}")

# --- UI Setup ---
root = tk.Tk()
root.title("Kahoot Number Generator")
root.geometry("500x550")

# Variables
zip_var = tk.BooleanVar(value=True)
os_logging_var = tk.BooleanVar(value=True)
root.os_logging_var = os_logging_var

# Header & Result
result_label = tk.Label(root, text="Click to generate", font=("Arial", 20))
result_label.pack(pady=30)

btn = tk.Button(root, text="Generate Code", command=generate_code,
                font=("Arial", 14, "bold"), bg="#46178f", fg="white", padx=20)
btn.pack(pady=10)

status_label = tk.Label(root, text="Not yet generated", fg="gray")
status_label.pack(pady=5)

# --- Settings Frame ---
options_frame = tk.LabelFrame(root, text=" Logging Settings ", padx=20, pady=10)
options_frame.pack(pady=15)

tk.Checkbutton(options_frame, text="Enable ZIP Compression", variable=zip_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Log OS Information", variable=os_logging_var).pack(anchor="w")

# --- Actions Frame ---
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

folder_btn = tk.Button(action_frame, text="📁 Open Log Folder", command=open_folder,
                       font=("Arial", 10), bg="#f2f2f2")
folder_btn.pack()

# Footer
os_Label = tk.Label(root, text=f"System: {platform.system()}", fg="blue")
credit_label = tk.Label(root, text="Created by @KeresDev and @TheMadPerson\nLicensed under GNU GPL-2.0\nOpen Source - DO NOT SELL",
                        font=("Arial", 8, "italic"), wraplength=350, justify="center", fg="gray")

credit_label.pack(side="bottom", pady=10)
os_Label.pack(side="bottom")

root.mainloop()
