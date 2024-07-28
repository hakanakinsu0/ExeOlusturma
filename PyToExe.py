import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import platform

def select_py_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    return file_path

def convert_to_exe(file_path):
    try:
        # Change directory to the location of the .py file
        file_directory = os.path.dirname(file_path)
        os.chdir(file_directory)

        # Run the pyinstaller command
        subprocess.run(["pyinstaller", "--onefile", "--hidden-import=pyodbc", "--hidden-import=pandas", "--hidden-import=sqlalchemy", file_path])

        # Inform the user about the completion
        print(f"{file_path} has been successfully converted to .exe")
        
        # Open the folder where the .exe file is saved
        dist_directory = os.path.join(file_directory, 'dist')
        open_folder(dist_directory)
    except Exception as e:
        print(f"An error occurred: {e}")

def open_folder(path):
    # Determine the platform and open the folder accordingly
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # Linux
        subprocess.Popen(["xdg-open", path])

if __name__ == "__main__":
    py_file_path = select_py_file()
    if py_file_path:
        convert_to_exe(py_file_path)
    else:
        print("No file was selected.")
