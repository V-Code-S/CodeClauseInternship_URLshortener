import tkinter as tk
import pyshorteners
import pyperclip

# Function to shorten the URL
def shorten_url():
    long_url = long_url_entry.get()
    api_key = '34980c0a48da4ea9da6c5d2357834e788ff052e1'  

    s = pyshorteners.Shortener(api_key=api_key)
    shortened_url = s.bitly.short(long_url)

    result_label.config(text=f"Shortened URL: {shortened_url}")
    
    # Enable the Copy button and store the shortened URL in a variable
    copy_button.config(state=tk.NORMAL)
    global copied_url
    copied_url = shortened_url

# Function to copy the URL to clipboard
def copy_url():
    if copied_url:
        pyperclip.copy(copied_url)
        copy_button.config(text="Copied!", state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("URL Shortener -by VIRUPAKSHI")

# Create and pack a label for instructions
instructions_label = tk.Label(root, text="Enter a long URL :")
instructions_label.pack(pady=10)

# Create and pack an entry widget for the long URL
long_url_entry = tk.Entry(root, width=40)
long_url_entry.pack()

# Create and pack a button to shorten the URL
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

# Create and pack a label for displaying the result
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

# Create and pack a button to copy the URL
copy_button = tk.Button(root, text="Copy", state=tk.DISABLED, command=copy_url)
copy_button.pack(pady=5)

# Initialize the copied URL variable
copied_url = None

# Run the GUI application
root.mainloop()
