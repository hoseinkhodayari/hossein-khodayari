import os

# ANSI color codes
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_welcome():
    clear_screen()
    print(GREEN + """
    ████████╗██╗██████╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗
    ╚══██╔══╝██║██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
       ██║   ██║██████╔╝    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
       ██║   ██║██╔═══╝     ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
       ██║   ██║██║         ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
       ╚═╝   ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """ + RESET)
    print(BLUE + "Welcome to the Tip Calculator!" + RESET)
    print("This program helps you calculate how much each person should pay after adding a tip.\n")

def get_valid_bill():
    while True:
        try:
            bill = float(input(YELLOW + "What was the total bill? $" + RESET))
            if bill <= 0:
                print(RED + "Bill amount must be greater than 0. Please try again." + RESET)
                continue
            return bill
        except ValueError:
            print(RED + "Invalid input. Please enter a valid number." + RESET)

def get_valid_tip():
    valid_tips = [0, 10, 12, 15]
    while True:
        try:
            tip = int(input(YELLOW + f"What tip would you like to give? {valid_tips} percent? " + RESET))
            if tip not in valid_tips:
                print(RED + f"Tip must be one of {valid_tips}. Please try again." + RESET)
                continue
            return tip
        except ValueError:
            print(RED + "Invalid input. Please enter a valid number." + RESET)

def get_valid_people():
    while True:
        try:
            people = int(input(YELLOW + "How many people to split the bill with? " + RESET))
            if people <= 0:
                print(RED + "Number of people must be greater than 0. Please try again." + RESET)
                continue
            return people
        except ValueError:
            print(RED + "Invalid input. Please enter a valid number." + RESET)

def calculate_and_display(bill, tip, people):
    total_with_tip = bill + (bill * (tip / 100))
    per_person = total_with_tip / people
    final_amount = round(per_person, 2)

    print(GREEN + "\n" + "="*50 + RESET)
    print(BLUE + f"Total bill: ${bill}" + RESET)
    print(BLUE + f"Tip percentage: {tip}%" + RESET)
    print(BLUE + f"Number of people: {people}" + RESET)
    print(BLUE + f"Total with tip: ${round(total_with_tip, 2)}" + RESET)
    print(GREEN + f"Each person should pay: ${final_amount}" + RESET)
    print(GREEN + "="*50 + RESET)

def main():
    print_welcome()
    while True:
        bill = get_valid_bill()
        tip = get_valid_tip()
        people = get_valid_people()
        calculate_and_display(bill, tip, people)

        again = input(YELLOW + "\nWould you like to calculate another bill? (y/n): " + RESET).lower()
        if again != 'y':
            print(GREEN + "Thank you for using the Tip Calculator! Goodbye." + RESET)
            break
        clear_screen()
        print_welcome()

if __name__ == "__main__":
    main()
