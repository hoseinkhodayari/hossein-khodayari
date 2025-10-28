"""
Prime Number Checker Program

This program defines a function to check if a number is prime and provides a simple user interface
to input a number and get the result.
"""

import math

def is_prime(n):
    """
    Check if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check divisibility from 3 to sqrt(n), skipping even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def main():
    """
    Main function to handle user input and output.
    """
    try:
        # Get user input
        num = int(input("Enter a number to check if it's prime: "))

        # Check if prime
        result = is_prime(num)

        # Display result
        if result:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()