import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from datetime import datetime

class CoffeeMachine:
    def __init__(self):
        # Coffee machine resources
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0.0
        }
        
        # Menu with ingredients and prices
        self.menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }
        
        # Coin values
        self.coin_values = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickels": 0.05,
            "pennies": 0.01
        }
        
        self.setup_gui()
    
    def setup_gui(self):
        """Setup the main GUI window with warm colors"""
        self.root = tk.Tk()
        self.root.title("☕ Coffee Machine")
        self.root.geometry("600x700")
        self.root.configure(bg='#8B4513')  # Saddle brown background
        self.root.resizable(False, False)
        
        # Configure style for warm colors
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Warm.TButton', 
                       background='#D2691E',
                       foreground='white',
                       font=('Arial', 12, 'bold'),
                       padding=10)
        
        style.map('Warm.TButton',
                 background=[('active', '#CD853F')])
        
        style.configure('Report.TButton',
                       background='#A0522D',
                       foreground='white',
                       font=('Arial', 10),
                       padding=5)
        
        style.map('Report.TButton',
                 background=[('active', '#8B4513')])
        
        # Main title with time
        title_frame = tk.Frame(self.root, bg='#8B4513')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame,
                              text="☕ COFFEE MACHINE ☕",
                              font=('Arial', 24, 'bold'),
                              bg='#8B4513',
                              fg='#F4A460')
        title_label.pack()
        
        # Time display
        self.time_label = tk.Label(title_frame,
                                  text="",
                                  font=('Arial', 10),
                                  bg='#8B4513',
                                  fg='#DEB887')
        self.time_label.pack()
        self.update_time()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#8B4513')
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Welcome message
        welcome_label = tk.Label(main_frame,
                                text="What would you like?",
                                font=('Arial', 18, 'bold'),
                                bg='#8B4513',
                                fg='#F5DEB3')
        welcome_label.pack(pady=20)
        
        # Drink selection frame
        drinks_frame = tk.Frame(main_frame, bg='#8B4513')
        drinks_frame.pack(pady=20)
        
        # Drink buttons
        self.create_drink_buttons(drinks_frame)
        
        # Control buttons frame
        control_frame = tk.Frame(main_frame, bg='#8B4513')
        control_frame.pack(pady=20)
        
        # Report and Off buttons
        report_btn = ttk.Button(control_frame,
                               text="📊 Report",
                               style='Report.TButton',
                               command=self.show_report)
        report_btn.pack(side='left', padx=10)
        
        off_btn = ttk.Button(control_frame,
                            text="🔴 Turn Off",
                            style='Report.TButton',
                            command=self.turn_off)
        off_btn.pack(side='right', padx=10)
        
        # Status display
        self.status_frame = tk.Frame(main_frame, bg='#DEB887', relief='raised', bd=2)
        self.status_frame.pack(fill='x', pady=20)
        
        self.status_label = tk.Label(self.status_frame,
                                    text="Welcome! Please select a drink.",
                                    font=('Arial', 12),
                                    bg='#DEB887',
                                    fg='#8B4513',
                                    wraplength=500)
        self.status_label.pack(pady=10)
        
        # Resources display (initially hidden)
        self.resources_frame = tk.Frame(main_frame, bg='#F5DEB3', relief='sunken', bd=2)
        self.resources_label = tk.Label(self.resources_frame,
                                       text="",
                                       font=('Courier', 11),
                                       bg='#F5DEB3',
                                       fg='#8B4513',
                                       justify='left')
        self.resources_label.pack(pady=10)
    
    def create_drink_buttons(self, parent):
        """Create drink selection buttons"""
        drinks_info = {
            "espresso": {"emoji": "☕", "color": "#8B4513"},
            "latte": {"emoji": "🥛", "color": "#D2691E"},
            "cappuccino": {"emoji": "☕", "color": "#CD853F"}
        }
        
        for drink in self.menu:
            drink_frame = tk.Frame(parent, bg='#8B4513')
            drink_frame.pack(pady=10)
            
            # Drink button
            btn = ttk.Button(drink_frame,
                           text=f"{drinks_info[drink]['emoji']} {drink.title()} - ${self.menu[drink]['cost']:.2f}",
                           style='Warm.TButton',
                           command=lambda d=drink: self.select_drink(d))
            btn.pack()
    
    def select_drink(self, drink):
        """Handle drink selection"""
        self.update_status(f"You selected {drink.title()}. Checking resources...")
        
        # Check if resources are sufficient
        if self.check_resources(drink):
            self.update_status(f"Resources sufficient for {drink.title()}. Please insert coins.")
            self.show_coin_input(drink)
        else:
            # Find which resource is insufficient
            for ingredient, amount in self.menu[drink]["ingredients"].items():
                if self.resources[ingredient] < amount:
                    self.update_status(f"Sorry, there is not enough {ingredient}.")
                    break
    
    def check_resources(self, drink):
        """Check if there are enough resources to make the drink"""
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            if self.resources[ingredient] < amount:
                return False
        return True
    
    def show_coin_input(self, drink):
        """Show coin input dialog"""
        coin_window = tk.Toplevel(self.root)
        coin_window.title("Insert Coins")
        coin_window.geometry("450x400")
        coin_window.configure(bg='#DEB887')
        coin_window.resizable(False, False)
        coin_window.grab_set()  # Make it modal
        
        # Center the window
        coin_window.transient(self.root)
        
        title_label = tk.Label(coin_window,
                              text=f"💰 Insert coins for {drink.title()} 💰",
                              font=('Arial', 16, 'bold'),
                              bg='#DEB887',
                              fg='#8B4513')
        title_label.pack(pady=15)
        
        cost_label = tk.Label(coin_window,
                             text=f"Cost: ${self.menu[drink]['cost']:.2f}",
                             font=('Arial', 14, 'bold'),
                             bg='#DEB887',
                             fg='#8B4513')
        cost_label.pack(pady=5)
        
        instruction_label = tk.Label(coin_window,
                                   text="Enter the number of each coin type:",
                                   font=('Arial', 11),
                                   bg='#DEB887',
                                   fg='#8B4513')
        instruction_label.pack(pady=5)
        
        # Coin input frame
        coin_frame = tk.Frame(coin_window, bg='#DEB887')
        coin_frame.pack(pady=15)
        
        coin_entries = {}
        
        for coin_type in self.coin_values:
            row_frame = tk.Frame(coin_frame, bg='#DEB887')
            row_frame.pack(pady=8, fill='x')
            
            label = tk.Label(row_frame,
                           text=f"{coin_type.title()} (${self.coin_values[coin_type]:.2f}):",
                           font=('Arial', 12),
                           bg='#DEB887',
                           fg='#8B4513',
                           width=18,
                           anchor='w')
            label.pack(side='left')
            
            entry = tk.Entry(row_frame, font=('Arial', 12), width=8, justify='center')
            entry.pack(side='right', padx=10)
            entry.insert(0, "0")
            coin_entries[coin_type] = entry
            
            # Add validation to only allow numbers
            entry.bind('<KeyPress>', self.validate_number_input)
        
        # Total display
        total_frame = tk.Frame(coin_window, bg='#F5DEB3', relief='raised', bd=2)
        total_frame.pack(pady=15, padx=20, fill='x')
        
        total_label = tk.Label(total_frame,
                              text="Total inserted: $0.00",
                              font=('Arial', 14, 'bold'),
                              bg='#F5DEB3',
                              fg='#8B4513')
        total_label.pack(pady=8)
        
        def update_total(*args):
            total = 0
            try:
                for coin_type, entry in coin_entries.items():
                    count = int(entry.get() or 0)
                    if count < 0:
                        entry.delete(0, tk.END)
                        entry.insert(0, "0")
                        count = 0
                    total += count * self.coin_values[coin_type]
                total_label.config(text=f"Total inserted: ${total:.2f}")
                
                # Update button color based on sufficient funds
                cost = self.menu[drink]["cost"]
                if total >= cost:
                    pay_btn.config(text=f"✅ Pay ${cost:.2f} (Sufficient)")
                else:
                    pay_btn.config(text=f"💰 Pay ${cost:.2f} (Need ${cost-total:.2f} more)")
                    
            except ValueError:
                total_label.config(text="Please enter valid numbers only")
        
        # Bind update function to all entries
        for entry in coin_entries.values():
            entry.bind('<KeyRelease>', update_total)
            entry.bind('<FocusOut>', update_total)
        
        # Buttons
        button_frame = tk.Frame(coin_window, bg='#DEB887')
        button_frame.pack(pady=20)
        
        def process_payment():
            try:
                total_inserted = 0
                for coin_type, entry in coin_entries.items():
                    count = int(entry.get() or 0)
                    if count < 0:
                        messagebox.showerror("Error", "Please enter positive numbers only.")
                        return
                    total_inserted += count * self.coin_values[coin_type]
                
                cost = self.menu[drink]["cost"]
                
                if total_inserted >= cost:
                    change = total_inserted - cost
                    self.resources["money"] += cost
                    
                    # Deduct ingredients
                    for ingredient, amount in self.menu[drink]["ingredients"].items():
                        self.resources[ingredient] -= amount
                    
                    coin_window.destroy()
                    self.show_purchase_success(drink, change)
                else:
                    messagebox.showwarning("Insufficient Payment",
                                         f"You need ${cost - total_inserted:.2f} more.\nCurrent total: ${total_inserted:.2f}")
                    
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for coin counts.")
        
        pay_btn = ttk.Button(button_frame,
                           text=f"💰 Pay ${self.menu[drink]['cost']:.2f}",
                           style='Warm.TButton',
                           command=process_payment)
        pay_btn.pack(side='left', padx=10)
        
        cancel_btn = ttk.Button(button_frame,
                              text="❌ Cancel",
                              style='Report.TButton',
                              command=coin_window.destroy)
        cancel_btn.pack(side='right', padx=10)
        
        # Initial update
        update_total()
    
    def validate_number_input(self, event):
        """Validate that only numbers are entered"""
        char = event.char
        if char.isdigit() or char in ['\b', '\x7f']:  # Allow digits, backspace, delete
            return True
        elif char == '' or event.keysym in ['Left', 'Right', 'Up', 'Down', 'Tab']:
            return True
        else:
            return "break"  # Prevent the character from being entered
    
    def show_purchase_success(self, drink, change):
        """Show purchase success dialog with thank you message"""
        success_window = tk.Toplevel(self.root)
        success_window.title("Purchase Successful!")
        success_window.geometry("450x300")
        success_window.configure(bg='#DEB887')
        success_window.resizable(False, False)
        success_window.grab_set()
        success_window.transient(self.root)
        
        # Success message
        success_label = tk.Label(success_window,
                                text="🎉 Purchase Successful! 🎉",
                                font=('Arial', 18, 'bold'),
                                bg='#DEB887',
                                fg='#8B4513')
        success_label.pack(pady=20)
        
        # Drink message
        drink_label = tk.Label(success_window,
                              text=f"Here is your {drink.title()}! ☕",
                              font=('Arial', 16),
                              bg='#DEB887',
                              fg='#8B4513')
        drink_label.pack(pady=10)
        
        # Change message if applicable
        if change > 0:
            change_label = tk.Label(success_window,
                                   text=f"Here is ${change:.2f} in change.",
                                   font=('Arial', 14),
                                   bg='#DEB887',
                                   fg='#8B4513')
            change_label.pack(pady=5)
        
        # Thank you message
        thank_you_label = tk.Label(success_window,
                                  text="Thank you for your purchase!",
                                  font=('Arial', 14, 'bold'),
                                  bg='#DEB887',
                                  fg='#8B4513')
        thank_you_label.pack(pady=15)
        
        # Ask for another order
        another_label = tk.Label(success_window,
                                text="Would you like to place another order?",
                                font=('Arial', 12),
                                bg='#DEB887',
                                fg='#8B4513')
        another_label.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(success_window, bg='#DEB887')
        button_frame.pack(pady=20)
        
        def continue_ordering():
            success_window.destroy()
            self.update_status("Welcome back! Please select another drink.")
        
        def finish_ordering():
            success_window.destroy()
            self.update_status("Thank you for using our Coffee Machine! Have a great day! ☕")
        
        yes_btn = ttk.Button(button_frame,
                           text="☕ Yes, Another Order",
                           style='Warm.TButton',
                           command=continue_ordering)
        yes_btn.pack(side='left', padx=10)
        
        no_btn = ttk.Button(button_frame,
                          text="👋 No, Thank You",
                          style='Report.TButton',
                          command=finish_ordering)
        no_btn.pack(side='right', padx=10)
        
        # Auto-close after 15 seconds if no response
        success_window.after(15000, continue_ordering)
    
    def show_report(self):
        """Display current resources"""
        report_text = f"""Current Resources:
Water: {self.resources['water']}ml
Milk: {self.resources['milk']}ml
Coffee: {self.resources['coffee']}g
Money: ${self.resources['money']:.2f}"""
        
        self.resources_label.config(text=report_text)
        self.resources_frame.pack(fill='x', pady=10)
        self.update_status("Resource report displayed above.")
        
        # Hide report after 10 seconds
        self.root.after(10000, lambda: self.resources_frame.pack_forget())
    
    def update_status(self, message):
        """Update the status display"""
        self.status_label.config(text=message)
        self.root.update()
    
    def turn_off(self):
        """Turn off the coffee machine"""
        result = messagebox.askyesno("Turn Off", "Are you sure you want to turn off the coffee machine?")
        if result:
            self.update_status("Coffee machine is turning off... Goodbye! 👋")
            self.root.after(2000, self.root.quit)
    
    def update_time(self):
        """Update the time display"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)  # Update every second
    
    def run(self):
        """Start the coffee machine"""
        self.root.mainloop()

# Create and run the coffee machine
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()
