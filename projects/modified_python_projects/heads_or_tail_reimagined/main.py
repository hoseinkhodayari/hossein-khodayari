import tkinter as tk
import random

class HeadsTailsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Heads or Tails Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#87CEEB")  # Sky blue background
        
        self.wins = 0
        self.losses = 0
        
        # Title
        self.title_label = tk.Label(root, text="Heads or Tails Game", font=("Arial", 20, "bold"), bg="#87CEEB", fg="white")
        self.title_label.pack(pady=10)
        
        # Instruction
        self.instruction_label = tk.Label(root, text="Choose Heads or Tails!", font=("Arial", 14), bg="#87CEEB", fg="white")
        self.instruction_label.pack(pady=5)
        
        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#87CEEB")
        self.button_frame.pack(pady=10)
        
        self.heads_button = tk.Button(self.button_frame, text="Heads", font=("Arial", 16), bg="green", fg="white", command=lambda: self.flip_coin("heads"))
        self.heads_button.pack(side=tk.LEFT, padx=10)
        
        self.tails_button = tk.Button(self.button_frame, text="Tails", font=("Arial", 16), bg="red", fg="white", command=lambda: self.flip_coin("tails"))
        self.tails_button.pack(side=tk.LEFT, padx=10)
        
        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#87CEEB")
        self.result_label.pack(pady=10)
        
        # Score frame
        self.score_frame = tk.Frame(root, bg="#87CEEB")
        self.score_frame.pack(pady=10)
        
        self.wins_label = tk.Label(self.score_frame, text=f"Wins: {self.wins}", font=("Arial", 14), bg="#87CEEB", fg="green")
        self.wins_label.pack(side=tk.LEFT, padx=20)
        
        self.losses_label = tk.Label(self.score_frame, text=f"Losses: {self.losses}", font=("Arial", 14), bg="#87CEEB", fg="red")
        self.losses_label.pack(side=tk.LEFT, padx=20)
        
        # Reset button
        self.reset_button = tk.Button(root, text="Reset Scores", font=("Arial", 12), bg="orange", fg="white", command=self.reset_scores)
        self.reset_button.pack(pady=10)
    
    def flip_coin(self, user_choice):
        self.heads_button.config(state=tk.DISABLED)
        self.tails_button.config(state=tk.DISABLED)
        self.result_label.config(text="Flipping...", fg="black")
        self.root.after(1500, lambda: self.show_result(user_choice))
    
    def show_result(self, user_choice):
        coin_result = random.choice(["heads", "tails"])
        if coin_result == user_choice:
            self.result_label.config(text=f"{coin_result.capitalize()}, you won!", fg="green")
            self.wins += 1
            self.wins_label.config(text=f"Wins: {self.wins}")
        else:
            self.result_label.config(text=f"{coin_result.capitalize()}, you lost!", fg="red")
            self.losses += 1
            self.losses_label.config(text=f"Losses: {self.losses}")
        
        self.heads_button.config(state=tk.NORMAL)
        self.tails_button.config(state=tk.NORMAL)
    
    def reset_scores(self):
        self.wins = 0
        self.losses = 0
        self.wins_label.config(text=f"Wins: {self.wins}")
        self.losses_label.config(text=f"Losses: {self.losses}")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = HeadsTailsGame(root)
    root.mainloop()