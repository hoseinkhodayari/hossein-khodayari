import tkinter as tk
from tkinter import messagebox, scrolledtext

# ASCII Art
art = """
___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\""""

# Global variables
bidders = {}

# Function to add a bidder
def add_bidder():
    name = name_entry.get().strip()
    try:
        bid = int(bid_entry.get().strip())
        if name and bid > 0:
            bidders[name] = bid
            update_bidder_list()
            name_entry.delete(0, tk.END)
            bid_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid name and positive bid amount")
    except ValueError:
        messagebox.showerror("Error", "Bid must be a number")

# Function to update the bidder list display
def update_bidder_list():
    bidder_list.delete(1.0, tk.END)
    for name, bid in bidders.items():
        bidder_list.insert(tk.END, f"{name}: ${bid}\n")

# Function to calculate winner
def calculate_winner():
    if not bidders:
        messagebox.showwarning("Warning", "No bidders added yet")
        return
    winner_name = max(bidders, key=bidders.get)
    winner_bid = bidders[winner_name]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"🏆 Winner: {winner_name} with ${winner_bid} bid!\n\n")
    result_text.insert(tk.END, "📊 Ranked Results:\n")
    sorted_bidders = sorted(bidders.items(), key=lambda x: x[1], reverse=True)
    for i, (name, bid) in enumerate(sorted_bidders, 1):
        result_text.insert(tk.END, f"{i}. {name}: ${bid}\n")

# Function to clear all
def clear_all():
    global bidders
    bidders = {}
    update_bidder_list()
    result_text.delete(1.0, tk.END)
    name_entry.delete(0, tk.END)
    bid_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Secret Auction - Black Flower Pot")
root.geometry("700x600")
root.configure(bg="#1E1E2E")  # Dark background

# ASCII Art Label
art_label = tk.Label(root, text=art, font=("Courier", 8), fg="#F38BA8", bg="#1E1E2E")
art_label.pack(pady=10)

# Welcome Label
welcome_label = tk.Label(root, text="Welcome to the Infamous Black Flower Pot Auction!", font=("Arial", 14, "bold"), fg="#89B4FA", bg="#1E1E2E")
welcome_label.pack(pady=5)
rules_label = tk.Label(root, text="Rules: Bidders place bids simultaneously. Highest bid wins!", font=("Arial", 10), fg="#CDD6F4", bg="#1E1E2E")
rules_label.pack(pady=5)

# Input Frame
input_frame = tk.Frame(root, bg="#1E1E2E")
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Bidder Name:", font=("Arial", 12), fg="#CDD6F4", bg="#1E1E2E")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
name_entry.grid(row=0, column=1, padx=5, pady=5)

bid_label = tk.Label(input_frame, text="Bid Amount ($):", font=("Arial", 12), fg="#CDD6F4", bg="#1E1E2E")
bid_label.grid(row=1, column=0, padx=5, pady=5)
bid_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
bid_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Bidder", command=add_bidder, bg="#A6E3A1", fg="#1E1E2E", font=("Arial", 12, "bold"))
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Bidder List
bidder_list_label = tk.Label(root, text="Current Bidders:", font=("Arial", 12, "bold"), fg="#CDD6F4", bg="#1E1E2E")
bidder_list_label.pack()
bidder_list = scrolledtext.ScrolledText(root, width=50, height=8, font=("Arial", 10), bg="#313244", fg="#CDD6F4")
bidder_list.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1E1E2E")
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate Winner", command=calculate_winner, bg="#F9E2AF", fg="#1E1E2E", font=("Arial", 12, "bold"), width=15)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all, bg="#F38BA8", fg="#1E1E2E", font=("Arial", 12, "bold"), width=15)
clear_button.grid(row=0, column=1, padx=10)

# Result Display
result_label = tk.Label(root, text="Results:", font=("Arial", 12, "bold"), fg="#CDD6F4", bg="#1E1E2E")
result_label.pack()
result_text = scrolledtext.ScrolledText(root, width=50, height=10, font=("Arial", 10), bg="#313244", fg="#CDD6F4")
result_text.pack(pady=5)

# Run the GUI
root.mainloop()