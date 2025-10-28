import tkinter as tk
from tkinter import messagebox

def is_leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year.

    A leap year is divisible by 4, but not by 100 unless also divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        ValueError: If the year is not a positive integer.
    """
    if not isinstance(year, int) or year <= 0:
        raise ValueError("Year must be a positive integer.")
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def check_leap_year():
    """Check if the entered year is a leap year and display the result."""
    try:
        year = int(entry.get())
        if is_leap_year(year):
            result_label.config(text=f"{year} is a leap year!", fg="green")
        else:
            result_label.config(text=f"{year} is not a leap year.", fg="red")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Leap Year Checker")
root.geometry("300x200")

# Create and place widgets
label = tk.Label(root, text="Enter a year:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", command=check_leap_year)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
