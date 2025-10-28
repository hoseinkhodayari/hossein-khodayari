import tkinter as tk
from tkinter import messagebox, ttk
import random

# Character sets
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '%', '&', '*', '(', ')', '-', '+', '=']

def generate_password():
    try:
        length_letters = int(spin_letters.get())
        length_numbers = int(spin_numbers.get())
        length_symbols = int(spin_symbols.get())

        include_letters = var_letters.get()
        include_numbers = var_numbers.get()
        include_symbols = var_symbols.get()

        if not (include_letters or include_numbers or include_symbols):
            messagebox.showerror("Error", "Please select at least one character type!")
            return

        total_length = (length_letters if include_letters else 0) + (length_numbers if include_numbers else 0) + (length_symbols if include_symbols else 0)
        if total_length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long!")
            return

        list_password = []

        if include_letters:
            for _ in range(length_letters):
                list_password.append(random.choice(letters))

        if include_numbers:
            for _ in range(length_numbers):
                list_password.append(random.choice(numbers))

        if include_symbols:
            for _ in range(length_symbols):
                list_password.append(random.choice(symbols))

        random.shuffle(list_password)

        final_password = "".join(list_password)
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, final_password)

        # Password strength
        strength = "Weak"
        if total_length >= 12 and include_letters and include_numbers and include_symbols:
            strength = "Strong"
        elif total_length >= 8 and (include_letters and include_numbers) or (include_letters and include_symbols) or (include_numbers and include_symbols):
            strength = "Medium"
        strength_label.config(text=f"Strength: {strength}", fg="green" if strength == "Strong" else "orange" if strength == "Medium" else "red")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def copy_to_clipboard():
    password = password_display.get(1.0, tk.END).strip()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create main window
root = tk.Tk()
root.title("PiPassword Generator")
root.geometry("500x600")
root.configure(bg='#e6f3ff')

# Title
title_label = tk.Label(root, text="Welcome to PiPassword Generator", font=("Arial", 16, "bold"), bg='#e6f3ff', fg='#003366')
title_label.pack(pady=20)

# Frame for inputs
input_frame = tk.Frame(root, bg='#e6f3ff')
input_frame.pack(pady=10)

# Checkboxes for types
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(input_frame, text="Include Letters", variable=var_letters, bg='#e6f3ff', font=("Arial", 10)).grid(row=0, column=0, sticky='w', padx=10)
tk.Checkbutton(input_frame, text="Include Numbers", variable=var_numbers, bg='#e6f3ff', font=("Arial", 10)).grid(row=1, column=0, sticky='w', padx=10)
tk.Checkbutton(input_frame, text="Include Symbols", variable=var_symbols, bg='#e6f3ff', font=("Arial", 10)).grid(row=2, column=0, sticky='w', padx=10)

# Spinboxes for lengths
tk.Label(input_frame, text="Letters:", bg='#e6f3ff', font=("Arial", 10)).grid(row=0, column=1, padx=10)
spin_letters = tk.Spinbox(input_frame, from_=0, to=20, width=5, font=("Arial", 10))
spin_letters.grid(row=0, column=2, padx=10)

tk.Label(input_frame, text="Numbers:", bg='#e6f3ff', font=("Arial", 10)).grid(row=1, column=1, padx=10)
spin_numbers = tk.Spinbox(input_frame, from_=0, to=20, width=5, font=("Arial", 10))
spin_numbers.grid(row=1, column=2, padx=10)

tk.Label(input_frame, text="Symbols:", bg='#e6f3ff', font=("Arial", 10)).grid(row=2, column=1, padx=10)
spin_symbols = tk.Spinbox(input_frame, from_=0, to=20, width=5, font=("Arial", 10))
spin_symbols.grid(row=2, column=2, padx=10)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg='#4CAF50', fg='white', font=("Arial", 12, "bold"), padx=20, pady=10)
generate_btn.pack(pady=20)

# Password display
password_display = tk.Text(root, height=2, width=40, font=("Courier", 14), bg='#ffffff', fg='#000000')
password_display.pack(pady=10)

# Strength label
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12), bg='#e6f3ff')
strength_label.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='#2196F3', fg='white', font=("Arial", 10), padx=10, pady=5)
copy_btn.pack(pady=10)

# Run the app
root.mainloop()