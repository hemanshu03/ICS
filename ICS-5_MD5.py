import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            md5_hash.update(data)  
    return md5_hash.hexdigest()
   
def check_md5(file_path, received_hash):
    file_hash = calculate_md5(file_path)
    return file_hash == received_hash

def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Choose a file")
    return file_path

file_path = choose_file()

if not file_path:
    print("No file selected. Exiting..")
    exit()

file_hash = calculate_md5(file_path)
print(f"MD5 Hash of {file_path}: {file_hash}")
received_hash = input("Enter the hash : ")

if check_md5(file_path, received_hash):
    print("File not been tampered.")
else:
    print("File tampered !")