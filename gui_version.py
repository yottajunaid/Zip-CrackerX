import os
import tkinter as tk
from tkinter import filedialog, messagebox
from subprocess import Popen, PIPE

from main import main

# Create Tkinter window
window = tk.Tk()
window.title("Zip File Brute Force GUI                                                         Developer: @YOTTAJUNAID")
window.configure(bg="black")


# Function to run the CLI version of the program
def run_cli_version():
    process = Popen(["python", "main.py"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    output_text.insert(tk.END, stdout.decode(), "red")
    output_text.insert(tk.END, stderr.decode(), "red")


# Function to select zip file
def select_zip_file():
    zip_file_path = filedialog.askopenfilename(title="Select Zip File", filetypes=[("Zip files", "*.zip")])
    zip_file_entry.delete(0, tk.END)
    zip_file_entry.insert(0, zip_file_path)


# Function to select wordlist
def select_wordlist():
    wordlist_path = filedialog.askopenfilename(title="Select Wordlist", filetypes=[("Text files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, wordlist_path)


# Function to Escape the ANSI escape codes in GUI
def strip_ansi_escape_codes(text):
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[-/]*[@-~])')
    return ansi_escape.sub('', text)
    # create a tag with red font color
    # output_text.tag_configure("red", foreground="red")


# Function to Start the BruteForce in GUI version with connection with the main.py
def start_bruteforce():
    zip_file_path = zip_file_entry.get()
    wordlist_path = wordlist_entry.get()
    bruteforce_inprogress.grid(row=5, columnspan=3)
    window.update()
    if os.path.exists(zip_file_path) and os.path.exists(wordlist_path):
        process = Popen(["python", "main.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate(f"{zip_file_path}\n{wordlist_path}\n".encode())
        # output_text.insert(tk.END,)
        output_text.insert(tk.END, strip_ansi_escape_codes(stdout.decode()), "red")
        # output_text.insert(tk.END,)
        output_text.insert(tk.END, strip_ansi_escape_codes(stderr.decode()), "red")
        output_text.see(tk.END)
        # t = Thread(target=perform_bruteforce, args=(zip_file_path, wordlist_path))
        # t.start()

    else:
        messagebox.showwarning("Warning", "Please select both a zip file and a wordlist.")


# Shows the Disclamer of this program
title_label = tk.Label(window,
                       text="This Tool only works with .ZIP file Protected with 'ZIP Legacy Encryption'\n"
                            "Github: https://github.com/yottajunaid",
                       bg="black", fg="red")
title_label.grid(row=0, columnspan=3)

# Label and entry for zip file
zip_file_label = tk.Label(window, text="Zip File:", bg="black", fg="red")
zip_file_label.grid(row=1, column=0, sticky="e")
zip_file_entry = tk.Entry(window, width=50)
zip_file_entry.grid(row=1, column=1, padx=5, pady=5)
zip_file_button = tk.Button(window, text="Browse", command=select_zip_file, bg="red", fg="black")
zip_file_button.grid(row=1, column=2, padx=5, pady=5)

# Label and entry for wordlist
wordlist_label = tk.Label(window, text="Wordlist:", bg="black", fg="red")
wordlist_label.grid(row=2, column=0, sticky="e")
wordlist_entry = tk.Entry(window, width=50)
wordlist_entry.grid(row=2, column=1, padx=5, pady=5)
wordlist_button = tk.Button(window, text="Browse", command=select_wordlist, bg="red", fg="black")
wordlist_button.grid(row=2, column=2, padx=5, pady=5)

# Button to start brute force attack
start_button = tk.Button(window, text="Start Bruteforce", command=start_bruteforce, bg="red", fg="black")
start_button.grid(row=3, columnspan=3, pady=10)

# Button to run CLI version
run_cli_button = tk.Button(window, text="Run CLI Version", command=run_cli_version, bg="red", fg="black")
run_cli_button.grid(row=4, columnspan=3, pady=10)

# Text widget to display output
output_text = tk.Text(window, height=10, width=70, bg="red", fg="black", font=("", 12, "bold"))
output_text.grid(row=6, columnspan=3, padx=10, pady=10)

# Shows bruteborfe running in background
bruteforce_inprogress = tk.Label(window,
                                 text="Bruteforce Attack is Activated in the Background\n "
                                      "You will be Notified after the attack is completed",
                                 bg="black", fg="red")

window.mainloop()

if __name__ == "__main__":
    main()
