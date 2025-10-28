import tkinter as tk
from tkinter import messagebox
import art

# Caesar Cipher function with fixes
def caesar_cipher(text, shift, direction):
    output = ""
    if direction == "decode":
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            output += chr(shifted)
        else:
            output += char
    return output

# Function to handle encode button
def encode():
    try:
        text = input_text.get()
        shift = int(shift_entry.get())
        result = caesar_cipher(text, shift, "encode")
        output_text.set(result)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer")

# Function to handle decode button
def decode():
    try:
        text = input_text.get()
        shift = int(shift_entry.get())
        result = caesar_cipher(text, shift, "decode")
        output_text.set(result)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer")

# Function to clear inputs
def clear():
    input_text.set("")
    shift_entry.delete(0, tk.END)
    output_text.set("")

# Create main window
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder")
root.geometry("600x500")
root.configure(bg="#2E3440")  # Dark background

# ASCII Art Label
art_label = tk.Label(root, text=art.art[0], font=("Courier", 10), fg="#88C0D0", bg="#2E3440")
art_label.pack(pady=10)

# Input Text Label and Entry
input_label = tk.Label(root, text="Enter your message:", font=("Arial", 12, "bold"), fg="#ECEFF4", bg="#2E3440")
input_label.pack()
input_text = tk.StringVar()
input_entry = tk.Entry(root, textvariable=input_text, width=50, font=("Arial", 12))
input_entry.pack(pady=5)

# Shift Label and Entry
shift_label = tk.Label(root, text="Enter shift number:", font=("Arial", 12, "bold"), fg="#ECEFF4", bg="#2E3440")
shift_label.pack()
shift_entry = tk.Entry(root, width=10, font=("Arial", 12))
shift_entry.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#2E3440")
button_frame.pack(pady=10)

encode_button = tk.Button(button_frame, text="Encode", command=encode, bg="#A3BE8C", fg="#2E3440", font=("Arial", 12, "bold"), width=10)
encode_button.grid(row=0, column=0, padx=10)

decode_button = tk.Button(button_frame, text="Decode", command=decode, bg="#BF616A", fg="#ECEFF4", font=("Arial", 12, "bold"), width=10)
decode_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear, bg="#D08770", fg="#2E3440", font=("Arial", 12, "bold"), width=10)
clear_button.grid(row=0, column=2, padx=10)

# Output Label and Text
output_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"), fg="#ECEFF4", bg="#2E3440")
output_label.pack()
output_text = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_text, width=50, font=("Arial", 12), state="readonly")
output_entry.pack(pady=5)

# Run the GUI
root.mainloop()