# !/usr/bin/env python3
"""this program is a number guessing game."""
import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("600x400")
        self.root.configure(bg='#FFA500')  # Orange background

        self.difficulty = None
        self.attempts = 0
        self.secret_number = 0
        self.min_num = 0
        self.max_num = 0
        self.current_attempts = 0

        self.frames = {}
        self.create_frames()
        self.show_frame("welcome")

    def create_frames(self):
        # Welcome frame
        self.frames["welcome"] = tk.Frame(self.root, bg='#FFA500')
        tk.Label(self.frames["welcome"], text="NUMBER GUESSING GAME", font=("Arial", 24, "bold"), bg='#FFA500', fg='#FFD700').pack(pady=20)
        tk.Label(self.frames["welcome"], text="Guess the secret number!", font=("Arial", 16), bg='#FFA500', fg='#FFFFFF').pack(pady=10)
        tk.Label(self.frames["welcome"], text="Choose your difficulty and range!", font=("Arial", 14), bg='#FFA500', fg='#FFFFFF').pack(pady=10)
        tk.Button(self.frames["welcome"], text="Start Game", command=self.show_difficulty, bg='#FF4500', fg='#FFFFFF', font=("Arial", 14)).pack(pady=20)

        # Difficulty frame
        self.frames["difficulty"] = tk.Frame(self.root, bg='#FFA500')
        tk.Label(self.frames["difficulty"], text="Choose Difficulty", font=("Arial", 20, "bold"), bg='#FFA500', fg='#FFD700').pack(pady=20)
        tk.Button(self.frames["difficulty"], text="Easy (15 attempts)", command=lambda: self.set_difficulty('easy', 15), bg='#32CD32', fg='#FFFFFF', font=("Arial", 12)).pack(pady=5)
        tk.Button(self.frames["difficulty"], text="Medium (10 attempts)", command=lambda: self.set_difficulty('medium', 10), bg='#FFD700', fg='#000000', font=("Arial", 12)).pack(pady=5)
        tk.Button(self.frames["difficulty"], text="Hard (5 attempts)", command=lambda: self.set_difficulty('hard', 5), bg='#FF6347', fg='#FFFFFF', font=("Arial", 12)).pack(pady=5)
        tk.Button(self.frames["difficulty"], text="God Mode (1 attempt, no hints)", command=lambda: self.set_difficulty('god', 1), bg='#8B0000', fg='#FFFFFF', font=("Arial", 12)).pack(pady=5)

        # Range frame
        self.frames["range"] = tk.Frame(self.root, bg='#FFA500')
        tk.Label(self.frames["range"], text="Choose Range", font=("Arial", 20, "bold"), bg='#FFA500', fg='#FFD700').pack(pady=20)
        tk.Label(self.frames["range"], text="Minimum number:", bg='#FFA500', fg='#FFFFFF', font=("Arial", 12)).pack()
        self.min_entry = tk.Entry(self.frames["range"], font=("Arial", 12))
        self.min_entry.pack(pady=5)
        tk.Label(self.frames["range"], text="Maximum number:", bg='#FFA500', fg='#FFFFFF', font=("Arial", 12)).pack()
        self.max_entry = tk.Entry(self.frames["range"], font=("Arial", 12))
        self.max_entry.pack(pady=5)
        tk.Button(self.frames["range"], text="Start Guessing", command=self.start_game, bg='#FF4500', fg='#FFFFFF', font=("Arial", 12)).pack(pady=20)

        # Game frame
        self.frames["game"] = tk.Frame(self.root, bg='#FFA500')
        self.attempts_label = tk.Label(self.frames["game"], text="", font=("Arial", 14), bg='#FFA500', fg='#FFFFFF')
        self.attempts_label.pack(pady=10)
        self.hint_label = tk.Label(self.frames["game"], text="", font=("Arial", 12), bg='#FFA500', fg='#FFFFFF')
        self.hint_label.pack(pady=10)
        tk.Label(self.frames["game"], text="Enter your guess:", bg='#FFA500', fg='#FFFFFF', font=("Arial", 12)).pack()
        self.guess_entry = tk.Entry(self.frames["game"], font=("Arial", 12))
        self.guess_entry.pack(pady=5)
        tk.Button(self.frames["game"], text="Guess", command=self.make_guess, bg='#FF4500', fg='#FFFFFF', font=("Arial", 12)).pack(pady=10)

        # Win/Lose frame
        self.frames["result"] = tk.Frame(self.root, bg='#FFA500')
        self.result_label = tk.Label(self.frames["result"], text="", font=("Arial", 18, "bold"), bg='#FFA500', fg='#FFD700')
        self.result_label.pack(pady=20)
        self.secret_label = tk.Label(self.frames["result"], text="", font=("Arial", 14), bg='#FFA500', fg='#FFFFFF')
        self.secret_label.pack(pady=10)
        tk.Button(self.frames["result"], text="Play Again", command=self.play_again, bg='#32CD32', fg='#FFFFFF', font=("Arial", 12)).pack(pady=10)
        tk.Button(self.frames["result"], text="Quit", command=self.root.quit, bg='#FF6347', fg='#FFFFFF', font=("Arial", 12)).pack(pady=5)

        for frame in self.frames.values():
            frame.pack(fill="both", expand=True)

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)

    def show_difficulty(self):
        self.show_frame("difficulty")

    def set_difficulty(self, diff, att):
        self.difficulty = diff
        self.attempts = att
        if diff == 'god':
            messagebox.showinfo("God Mode", "God Mode activated! One chance, no hints. Good luck!")
        self.show_frame("range")

    def start_game(self):
        try:
            self.min_num = int(self.min_entry.get())
            self.max_num = int(self.max_entry.get())
            if self.min_num >= self.max_num:
                messagebox.showerror("Error", "Minimum must be less than maximum!")
                return
            self.secret_number = random.randint(self.min_num, self.max_num)
            self.current_attempts = 0
            self.attempts_label.config(text=f"I've picked a number between {self.min_num} and {self.max_num}. You have {self.attempts} attempts.")
            self.hint_label.config(text="")
            self.guess_entry.delete(0, tk.END)
            self.show_frame("game")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.current_attempts += 1
            self.guess_entry.delete(0, tk.END)

            if guess == self.secret_number:
                self.result_label.config(text="YOU WIN!", fg='#32CD32')
                self.secret_label.config(text="Congratulations! You guessed it!")
                self.show_frame("result")
            elif self.current_attempts >= self.attempts:
                self.result_label.config(text="GAME OVER!", fg='#FF6347')
                self.secret_label.config(text=f"The secret number was {self.secret_number}. Better luck next time!")
                self.show_frame("result")
            else:
                if self.difficulty != 'god':
                    if guess < self.secret_number:
                        self.hint_label.config(text="Too low! Try higher.", fg='#0000FF')
                    else:
                        self.hint_label.config(text="Too high! Try lower.", fg='#0000FF')
                self.attempts_label.config(text=f"Attempt {self.current_attempts}/{self.attempts}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def play_again(self):
        self.show_frame("welcome")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()