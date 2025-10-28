import random
import time

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Colored ASCII art
ROCK = f"""
    {BLUE}_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___){RESET}
"""

PAPER = f"""
    {GREEN}_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________){RESET}
"""

SCISSORS = f"""
    {RED}_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___){RESET}
"""

RPS = [ROCK, PAPER, SCISSORS]

def print_colored(text, color):
    print(f"{color}{text}{RESET}")

def get_user_choice():
    while True:
        try:
            choice = input(f"{CYAN}Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: {RESET}")
            choice = int(choice)
            if choice in [0, 1, 2]:
                return choice
            else:
                print_colored("Invalid choice! Please enter 0, 1, or 2.", RED)
        except ValueError:
            print_colored("Invalid input! Please enter a number.", RED)

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        return "win"
    else:
        return "lose"

def play_round(round_num, user_score, comp_score):
    print(f"\n{YELLOW}--- Round {round_num} ---{RESET}")
    time.sleep(0.5)

    user_choice = get_user_choice()
    print(f"\n{MAGENTA}You chose:{RESET}")
    print(RPS[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"{MAGENTA}Computer chose:{RESET}")
    print(RPS[computer_choice])
    time.sleep(1)

    result = determine_winner(user_choice, computer_choice)
    if result == "win":
        print_colored("You win this round!", GREEN)
        user_score += 1
    elif result == "lose":
        print_colored("You lose this round!", RED)
        comp_score += 1
    else:
        print_colored("It's a draw!", YELLOW)

    return user_score, comp_score

def main():
    print_colored("🎮 Welcome to Rock-Paper-Scissors! 🎮", CYAN)
    print_colored("Let's play a best-of series!", YELLOW)

    while True:
        try:
            rounds = int(input(f"{CYAN}How many rounds would you like to play? {RESET}"))
            if rounds > 0:
                break
            else:
                print_colored("Please enter a positive number.", RED)
        except ValueError:
            print_colored("Invalid input! Please enter a number.", RED)

    user_score = 0
    comp_score = 0
   

    for round_num in range(1, rounds + 1):
        user_score, comp_score = play_round(round_num, user_score, comp_score)

    print(f"\n{YELLOW}--- Final Score ---{RESET}")
    print_colored(f"You: {user_score}", GREEN if user_score > comp_score else RED)
    print_colored(f"Computer: {comp_score}", RED if comp_score > user_score else GREEN)

    if user_score > comp_score:
        print_colored("🎉 Congratulations! You won the series! 🎉", GREEN)
    elif comp_score > user_score:
        print_colored("😢 Sorry, you lost the series. Better luck next time!", RED)
    else:
        print_colored("🤝 It's a tie series!", YELLOW)

    play_again = input(f"{CYAN}Do you want to play again? (y/n): {RESET}").lower()
    if play_again == 'y':
        main()
    else:
        print_colored("Thanks for playing! Goodbye! 👋", MAGENTA)

if __name__ == "__main__":
    main()
