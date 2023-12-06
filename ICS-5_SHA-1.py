import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_sha1(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha1_hash.update(data)
    return sha1_hash.hexdigest()

def check_file_integrity(received_hash, file_path):
    current_hash = calculate_sha1(file_path)
    return current_hash == received_hash

def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Choose a file")
    return file_path

if __name__ == "__main__":
    file_path = choose_file()

    if not file_path:
        print("No file selected. Exiting..")
        exit()

    hash_value = calculate_sha1(file_path)
    print(f'Hash: {hash_value}')
    received_hash = input("Enter the received SHA-1 hash: ")

    if check_file_integrity(received_hash, file_path):
        print("File is not tampered.")
    else:
        print("File has been tampered.")
