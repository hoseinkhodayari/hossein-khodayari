import tkinter as tk
import random
from game_data import game_data
from art import logo

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Higher Lower Game")
        self.root.geometry("1000x700")
        self.root.configure(bg='#F5F5DC')  # Beige background
        self.score = 0
        self.images = {}
        self.current_a = random.choice(game_data)
        self.current_b = random.choice(game_data)
        while self.current_b == self.current_a:
            self.current_b = random.choice(game_data)
        self.setup_ui()
        self.root.mainloop()

    def setup_ui(self):
        # Logo
        try:
            self.logo_img = tk.PhotoImage(file='images/logo.png')
            logo_label = tk.Label(self.root, image=self.logo_img, bg='#F5F5DC')
        except:
            logo_label = tk.Label(self.root, text=logo, font=('Courier', 10), bg='#F5F5DC', fg='#8B4513')
        logo_label.pack(pady=10)

        # Credits button
        credits_button = tk.Button(self.root, text="Credits", command=self.show_credits, font=('Times New Roman', 12), bg='#DEB887', fg='#8B4513', relief='raised', bd=3)
        credits_button.pack(pady=5)

        # Score
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=('Times New Roman', 16, 'bold'), bg='#F5F5DC', fg='#8B4513')
        self.score_label.pack()

        # Frame for two options
        frame = tk.Frame(self.root, bg='#F5F5DC')
        frame.pack(pady=20)

        # Left: A
        self.a_frame = tk.Frame(frame, bg='#F5F5DC', relief='raised', bd=2)
        self.a_frame.pack(side=tk.LEFT, padx=20)
        # Image
        self.a_image_label = tk.Label(self.a_frame, bg='#F5F5DC')
        self.load_image(self.current_a, self.a_image_label)
        self.a_image_label.pack()
        self.a_name = tk.Label(self.a_frame, text=self.current_a['name'], font=('Times New Roman', 14, 'bold'), bg='#F5F5DC', fg='#8B4513')
        self.a_name.pack()
        self.a_followers = tk.Label(self.a_frame, text=f"Followers: {self.current_a['followers']:,}", font=('Times New Roman', 12), bg='#F5F5DC', fg='#8B4513')
        self.a_followers.pack()
        self.a_nationality = tk.Label(self.a_frame, text=f"Nationality: {self.current_a['nationality']}", font=('Times New Roman', 12), bg='#F5F5DC', fg='#8B4513')
        self.a_nationality.pack()
        self.a_profession = tk.Label(self.a_frame, text=f"Profession: {self.current_a['profession']}", font=('Times New Roman', 12), bg='#F5F5DC', fg='#8B4513')
        self.a_profession.pack()

        # VS
        vs_label = tk.Label(frame, text="VS", font=('Times New Roman', 18, 'bold'), bg='#F5F5DC', fg='#DAA520')  # Goldenrod
        vs_label.pack(side=tk.LEFT, padx=20)

        # Right: B
        self.b_frame = tk.Frame(frame, bg='#F5F5DC', relief='raised', bd=2)
        self.b_frame.pack(side=tk.LEFT, padx=20)
        # Image
        self.b_image_label = tk.Label(self.b_frame, bg='#F5F5DC')
        self.load_image(self.current_b, self.b_image_label)
        self.b_image_label.pack()
        self.b_name = tk.Label(self.b_frame, text=self.current_b['name'], font=('Times New Roman', 14, 'bold'), bg='#F5F5DC', fg='#8B4513')
        self.b_name.pack()
        self.b_followers = tk.Label(self.b_frame, text="Followers: ???", font=('Times New Roman', 12), bg='#F5F5DC', fg='#8B4513')
        self.b_followers.pack()
        self.b_nationality = tk.Label(self.b_frame, text=f"Nationality: {self.current_b['nationality']}", font=('Times New Roman', 12), bg='#F5F5DC', fg='#8B4513')
        self.b_nationality.pack()
        self.b_profession = tk.Label(self.b_frame, text=f"Profession: {self.current_b['profession']}", font=('Times New Roman', 12), bg='#F5F5DC', fg='#8B4513')
        self.b_profession.pack()

        # Buttons
        button_frame = tk.Frame(self.root, bg='#F5F5DC')
        button_frame.pack(pady=20)
        self.a_button = tk.Button(button_frame, text="Choose A", command=self.choose_a, font=('Times New Roman', 14), bg='#DEB887', fg='#8B4513')  # Burlywood
        self.a_button.pack(side=tk.LEFT, padx=10)
        self.b_button = tk.Button(button_frame, text="Choose B", command=self.choose_b, font=('Times New Roman', 14), bg='#DEB887', fg='#8B4513')
        self.b_button.pack(side=tk.LEFT, padx=10)

    def choose_a(self):
        if self.current_a['followers'] >= self.current_b['followers']:
            self.score += 1
            self.update_score()
            self.next_round(winner='a')
        else:
            self.game_over()

    def choose_b(self):
        if self.current_b['followers'] >= self.current_a['followers']:
            self.score += 1
            self.update_score()
            self.next_round(winner='b')
        else:
            self.game_over()

    def next_round(self, winner):
        if winner == 'a':
            self.current_b = random.choice(game_data)
            while self.current_b == self.current_a:
                self.current_b = random.choice(game_data)
        else:
            self.current_a = self.current_b
            self.current_b = random.choice(game_data)
            while self.current_b == self.current_a:
                self.current_b = random.choice(game_data)
        self.update_ui()

    def update_ui(self):
        self.load_image(self.current_a, self.a_image_label)
        self.a_name.config(text=self.current_a['name'])
        self.a_followers.config(text=f"Followers: {self.current_a['followers']:,}")
        self.a_nationality.config(text=f"Nationality: {self.current_a['nationality']}")
        self.a_profession.config(text=f"Profession: {self.current_a['profession']}")
        self.load_image(self.current_b, self.b_image_label)
        self.b_name.config(text=self.current_b['name'])
        self.b_followers.config(text="Followers: ???")
        self.b_nationality.config(text=f"Nationality: {self.current_b['nationality']}")
        self.b_profession.config(text=f"Profession: {self.current_b['profession']}")

    def update_score(self):
        self.animate_score(0, self.score)

    def animate_score(self, current, target):
        if current < target:
            self.score_label.config(text=f"Score: {current}")
            self.root.after(50, self.animate_score, current + 1, target)
        else:
            self.score_label.config(text=f"Score: {self.score}")

    def game_over(self):
        # Show final score and restart
        result = tk.Toplevel(self.root)
        result.title("Game Over")
        result.geometry("300x200")
        result.configure(bg='#F5F5DC')
        tk.Label(result, text=f"Game Over!\nFinal Score: {self.score}", font=('Times New Roman', 16), bg='#F5F5DC', fg='#8B4513').pack(pady=20)
        tk.Button(result, text="Play Again", command=lambda: self.restart(result), font=('Times New Roman', 14), bg='#DEB887', fg='#8B4513').pack()

    def restart(self, result):
        result.destroy()
        self.score = 0
        self.current_a = random.choice(game_data)
        self.current_b = random.choice(game_data)
        while self.current_b == self.current_a:
            self.current_b = random.choice(game_data)
        self.update_score()
        self.update_ui()

    def load_image(self, entity, label):
        image_path = entity.get('image', '')
        if image_path and image_path not in self.images:
            try:
                self.images[image_path] = tk.PhotoImage(file=image_path).subsample(2, 2)  # Resize if needed
            except:
                self.images[image_path] = None
        if self.images.get(image_path):
            label.config(image=self.images[image_path])
        else:
            label.config(image='', text='No Image')

    def show_credits(self):
        credits_window = tk.Toplevel(self.root)
        credits_window.title("Credits")
        credits_window.geometry("500x300")
        credits_window.configure(bg='#F5F5DC')
        text = """Created by Hossein Khodayari
All rights reserved.

GitHub: https://github.com/hoseinkhodayari/hossein-khodayari
LinkedIn: www.linkedin.com/in/hossein-khodayari-0bb03032a"""
        label = tk.Label(credits_window, text=text, font=('Times New Roman', 14), bg='#F5F5DC', fg='#8B4513', justify='center', relief='ridge', bd=5)
        label.pack(expand=True, fill='both', padx=20, pady=20)

if __name__ == "__main__":
    Game()