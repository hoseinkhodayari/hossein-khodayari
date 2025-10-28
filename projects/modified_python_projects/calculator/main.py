# a working calculator with 4 functions or more:

# Colors for terminal UI
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

print(BLUE + BOLD + "welcome to the python calculator built by hossein khodayari, this calculator is capable of performing 4 main mathematical operation,\n add, subtract, multiply and divide numbers together." + END)
calculator_art = LIGHT_WHITE + """ _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""
print(calculator_art)


def addition (no1, no2):
    """this function performs the basic addition function of the first number on the second number."""
    return no1 + no2
add = addition

def subtraction (no1, no2):
    """this function performs the basic subtraction function of the first number on the second number."""
    return no1 - no2
subtract = subtraction

def multiplication (no1, no2):
    """this function performs the basic multiplication function of the first number on the second number."""
    return no1 * no2
multiply = multiplication

def division (no1, no2):
    """this function performs the basic division function of the first number on the second number."""
    return no1 / no2
divide = division

mathematical_operations = {"+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

first_num = float(input("what is your first number user? "))
operation_type = input("what operation will you choose?\n(+,-,*,/) ")
second_num = float(input("what is your second number user? "))
# def calculation (no1, no2):
#     """main function for calculating anything the user wants.(includes the MOs)"""
if operation_type == "+":
    print(mathematical_operations["+"](first_num, second_num))
elif operation_type == "-":
    print(mathematical_operations["-"](first_num, second_num))
elif operation_type == "*":
    print(mathematical_operations["*"](first_num, second_num))
elif operation_type == "/":
    print(mathematical_operations["/"](first_num, second_num))
    
      