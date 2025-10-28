"""
BMI Calculator

A user-friendly BMI calculator that takes weight in kg and height in meters.
"""
# colors
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'


print(BLUE + "this is a BMI calculator that calculates your body's BMI based on your given data.\n to begin, enter the required information below:" + GREEN)
def calculate_bmi():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight <= 0:
                print("Weight must be positive. Try again.")
                continue
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Height must be positive. Try again.")
                continue
            bmi = weight / (height ** 2)
            bmi_rounded = round(bmi, 1)
            print(f"Your BMI is {bmi_rounded}.")
            if bmi < 18.5:
                category = "underweight"
            elif 18.5 <= bmi < 25:
                category = "normal weight"
            elif 25 <= bmi < 30:
                category = "overweight"
            else:
                category = "obese"
            print(f"You are {category}.")
            again = input("Calculate again? (y/n): ").lower()
            if again != 'y':
                break
            else:
                print(BLUE+"thanks for using the program, goodbye.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculate_bmi()
