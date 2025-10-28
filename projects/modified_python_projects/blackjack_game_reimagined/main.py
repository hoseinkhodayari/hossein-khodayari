import tkinter as tk
from tkinter import messagebox, font
import random
import sys

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.symbols = {'hearts': '♥', 'diamonds': '♦', 'clubs': '♣', 'spades': '♠'}

    def __str__(self):
        return f"{self.value}{self.symbols[self.suit]}"

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Enhanced")
        self.root.geometry("1000x800")
        self.root.configure(bg='#0A5D36')  # Dark green background

        # Game variables
        self.money = 1000
        self.bet = 0
        self.bet_increment = 10
        self.game_state = "betting"  # betting, playing, round_over
        self.player_blackjack = False
        self.dealer_blackjack = False

        # Create card deck
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

        # Custom fonts
        self.title_font = font.Font(family="Arial", size=28, weight="bold")
        self.large_font = font.Font(family="Arial", size=20, weight="bold")
        self.medium_font = font.Font(family="Arial", size=16)
        self.small_font = font.Font(family="Arial", size=12)

        # Colors
        self.colors = {
            'dark_green': '#0A5D36',
            'light_green': '#2E8B57',
            'cream': '#FFFDD0',
            'red': '#DC143C',
            'black': '#000000',
            'white': '#FFFFFF',
            'gold': '#D4AF37'
        }

        # Create UI
        self.create_widgets()
        self.update_display()

    def create_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [Card(suit, value) for suit in suits for value in values]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self, hand):
        if len(self.deck) == 0:
            self.deck = self.create_deck()
            self.shuffle_deck()
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        value = 0
        aces = 0

        for card in hand:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
                value += 11
            else:
                value += int(card.value)

        # Adjust for aces if needed
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(
            self.root, 
            text="BLACKJACK", 
            font=self.title_font,
            fg=self.colors['gold'],
            bg=self.colors['dark_green']
        )
        self.title_label.pack(pady=20)
        
        # Money and bet frame
        info_frame = tk.Frame(self.root, bg=self.colors['dark_green'])
        info_frame.pack(pady=10)
        
        self.money_label = tk.Label(
            info_frame,
            text=f"Money: ${self.money}",
            font=self.large_font,
            fg=self.colors['cream'],
            bg=self.colors['dark_green']
        )
        self.money_label.pack(side=tk.LEFT, padx=20)
        
        self.bet_label = tk.Label(
            info_frame,
            text=f"Bet: ${self.bet}",
            font=self.large_font,
            fg=self.colors['cream'],
            bg=self.colors['dark_green']
        )
        self.bet_label.pack(side=tk.RIGHT, padx=20)
        
        # Dealer's hand frame
        dealer_frame = tk.Frame(self.root, bg=self.colors['dark_green'])
        dealer_frame.pack(pady=20)
        
        tk.Label(
            dealer_frame,
            text="Dealer's Hand:",
            font=self.medium_font,
            fg=self.colors['white'],
            bg=self.colors['dark_green']
        ).pack()
        
        self.dealer_hand_label = tk.Label(
            dealer_frame,
            text="",
            font=self.medium_font,
            fg=self.colors['cream'],
            bg=self.colors['dark_green'],
            justify=tk.LEFT
        )
        self.dealer_hand_label.pack()
        
        self.dealer_value_label = tk.Label(
            dealer_frame,
            text="Value: 0",
            font=self.medium_font,
            fg=self.colors['cream'],
            bg=self.colors['dark_green']
        )
        self.dealer_value_label.pack()
        
        # Player's hand frame
        player_frame = tk.Frame(self.root, bg=self.colors['dark_green'])
        player_frame.pack(pady=20)
        
        tk.Label(
            player_frame,
            text="Your Hand:",
            font=self.medium_font,
            fg=self.colors['white'],
            bg=self.colors['dark_green']
        ).pack()
        
        self.player_hand_label = tk.Label(
            player_frame,
            text="",
            font=self.medium_font,
            fg=self.colors['cream'],
            bg=self.colors['dark_green'],
            justify=tk.LEFT
        )
        self.player_hand_label.pack()
        
        self.player_value_label = tk.Label(
            player_frame,
            text="Value: 0",
            font=self.medium_font,
            fg=self.colors['cream'],
            bg=self.colors['dark_green']
        )
        self.player_value_label.pack()
        
        # Message label
        self.message_label = tk.Label(
            self.root,
            text="Place your bet to start the game",
            font=self.medium_font,
            fg=self.colors['gold'],
            bg=self.colors['dark_green']
        )
        self.message_label.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg=self.colors['dark_green'])
        button_frame.pack(pady=30)
        
        # Betting buttons
        self.bet_minus_button = tk.Button(
            button_frame,
            text="-",
            font=self.large_font,
            width=4,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.decrease_bet
        )
        self.bet_minus_button.grid(row=0, column=0, padx=10)
        
        self.deal_button = tk.Button(
            button_frame,
            text="Deal",
            font=self.large_font,
            width=8,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.deal_cards
        )
        self.deal_button.grid(row=0, column=1, padx=10)
        
        self.bet_plus_button = tk.Button(
            button_frame,
            text="+",
            font=self.large_font,
            width=4,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.increase_bet
        )
        self.bet_plus_button.grid(row=0, column=2, padx=10)
        
        # Game buttons (initially disabled)
        self.hit_button = tk.Button(
            button_frame,
            text="Hit",
            font=self.large_font,
            width=8,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.hit,
            state=tk.DISABLED
        )
        self.hit_button.grid(row=1, column=0, pady=10, padx=10)
        
        self.stand_button = tk.Button(
            button_frame,
            text="Stand",
            font=self.large_font,
            width=8,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.stand,
            state=tk.DISABLED
        )
        self.stand_button.grid(row=1, column=1, pady=10, padx=10)
        
        self.new_round_button = tk.Button(
            button_frame,
            text="New Round",
            font=self.large_font,
            width=8,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.new_round,
            state=tk.DISABLED
        )
        self.new_round_button.grid(row=1, column=2, pady=10, padx=10)

        # Double down button
        self.double_down_button = tk.Button(
            button_frame,
            text="Double Down",
            font=self.large_font,
            width=10,
            bg=self.colors['light_green'],
            fg=self.colors['black'],
            command=self.double_down,
            state=tk.DISABLED
        )
        self.double_down_button.grid(row=1, column=3, pady=10, padx=10)

        # Help button
        self.help_button = tk.Button(
            button_frame,
            text="Help",
            font=self.medium_font,
            width=6,
            bg=self.colors['gold'],
            fg=self.colors['black'],
            command=self.show_help
        )
        self.help_button.grid(row=2, column=1, pady=10, padx=10)

    def increase_bet(self):
        if self.game_state == "betting":
            if self.bet + self.bet_increment <= self.money:
                self.bet += self.bet_increment
                self.update_display()

    def decrease_bet(self):
        if self.game_state == "betting":
            if self.bet - self.bet_increment >= 0:
                self.bet -= self.bet_increment
                self.update_display()

    def deal_cards(self):
        if self.game_state == "betting" and self.bet > 0:
            self.game_state = "playing"
            self.money -= self.bet
            self.player_hand = []
            self.dealer_hand = []
            self.deck = self.create_deck()
            self.shuffle_deck()
            
            # Deal initial cards
            self.deal_card(self.player_hand)
            self.deal_card(self.dealer_hand)
            self.deal_card(self.player_hand)
            self.deal_card(self.dealer_hand)
            
            # Enable/disable buttons
            self.hit_button.config(state=tk.NORMAL)
            self.stand_button.config(state=tk.NORMAL)
            self.double_down_button.config(state=tk.NORMAL if len(self.player_hand) == 2 and self.money >= self.bet else tk.DISABLED)
            self.deal_button.config(state=tk.DISABLED)
            self.bet_plus_button.config(state=tk.DISABLED)
            self.bet_minus_button.config(state=tk.DISABLED)

            # Check for player blackjack
            player_value = self.calculate_hand_value(self.player_hand)
            if player_value == 21:
                self.player_blackjack = True
                self.stand()
            else:
                self.player_blackjack = False

            # Check for dealer blackjack
            dealer_value = self.calculate_hand_value(self.dealer_hand)
            if dealer_value == 21:
                self.dealer_blackjack = True
                if self.player_blackjack:
                    self.message_label.config(text="Both have Blackjack! Push.")
                    self.money += self.bet
                else:
                    self.message_label.config(text="Dealer has Blackjack! You lose.")
                self.game_state = "round_over"
                self.end_round()
            else:
                self.dealer_blackjack = False

            self.update_display()

    def hit(self):
        if self.game_state == "playing":
            self.deal_card(self.player_hand)
            self.double_down_button.config(state=tk.DISABLED)
            player_value = self.calculate_hand_value(self.player_hand)

            if player_value > 21:
                self.message_label.config(text="Bust! You went over 21.")
                self.game_state = "round_over"
                self.end_round()
            elif player_value == 21:
                self.stand()

            self.update_display()

    def double_down(self):
        if self.game_state == "playing" and len(self.player_hand) == 2 and self.money >= self.bet:
            self.money -= self.bet
            self.bet *= 2
            self.deal_card(self.player_hand)
            self.double_down_button.config(state=tk.DISABLED)
            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)
            self.stand()
            self.update_display()

    def stand(self):
        if self.game_state == "playing":
            self.game_state = "round_over"
            self.double_down_button.config(state=tk.DISABLED)
            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)

            # Dealer draws until value is 17 or higher
            while self.calculate_hand_value(self.dealer_hand) < 17:
                self.deal_card(self.dealer_hand)

            self.end_round()

    def end_round(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        # Determine winner
        if self.dealer_blackjack and not self.player_blackjack:
            message = "Dealer has Blackjack! You lose."
        elif self.player_blackjack and not self.dealer_blackjack:
            message = "Blackjack! You win!"
            self.money += int(self.bet * 1.5)
        elif self.player_blackjack and self.dealer_blackjack:
            message = "Both have Blackjack! Push."
            self.money += self.bet
        elif player_value > 21:
            message = "Bust! You lose."
        elif dealer_value > 21:
            message = "Dealer busts! You win!"
            self.money += self.bet * 2
        elif player_value > dealer_value:
            message = "You win!"
            self.money += self.bet * 2
        elif player_value < dealer_value:
            message = "Dealer wins."
        else:
            message = "Push! It's a tie."
            self.money += self.bet

        self.message_label.config(text=message)

        # Enable/disable buttons
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_down_button.config(state=tk.DISABLED)
        self.new_round_button.config(state=tk.NORMAL)

        self.update_display()

    def new_round(self):
        self.game_state = "betting"
        self.bet = 0
        self.player_blackjack = False
        self.dealer_blackjack = False

        # Enable/disable buttons
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_down_button.config(state=tk.DISABLED)
        self.new_round_button.config(state=tk.DISABLED)
        self.deal_button.config(state=tk.NORMAL)
        self.bet_plus_button.config(state=tk.NORMAL)
        self.bet_minus_button.config(state=tk.NORMAL)

        # Check if player is out of money
        if self.money <= 0:
            result = messagebox.askquestion("Game Over", "You're out of money! Would you like to start over?")
            if result == 'yes':
                self.money = 1000
            else:
                self.root.quit()

        self.update_display()

    def update_display(self):
        # Update money and bet labels
        self.money_label.config(text=f"Money: ${self.money}")
        self.bet_label.config(text=f"Bet: ${self.bet}")

        # Update hand displays
        if self.dealer_hand:
            if self.game_state == "playing":
                # Show only one dealer card during play
                dealer_text = f"{str(self.dealer_hand[0])}, ???"
                self.dealer_value_label.config(text="Value: ?")
            else:
                # Show all dealer cards after round ends
                dealer_text = ", ".join([str(card) for card in self.dealer_hand])
                self.dealer_value_label.config(text=f"Value: {self.calculate_hand_value(self.dealer_hand)}")
            self.dealer_hand_label.config(text=dealer_text)
        else:
            self.dealer_hand_label.config(text="")
            self.dealer_value_label.config(text="Value: 0")

        if self.player_hand:
            player_text = ", ".join([str(card) for card in self.player_hand])
            self.player_hand_label.config(text=player_text)
            self.player_value_label.config(text=f"Value: {self.calculate_hand_value(self.player_hand)}")
        else:
            self.player_hand_label.config(text="")
            self.player_value_label.config(text="Value: 0")

        # Update button states based on game state
        if self.game_state == "betting":
            self.deal_button.config(state=tk.NORMAL if self.bet > 0 else tk.DISABLED)
            self.bet_plus_button.config(state=tk.NORMAL if self.bet < self.money else tk.DISABLED)
            self.bet_minus_button.config(state=tk.NORMAL if self.bet > 0 else tk.DISABLED)

    def show_help(self):
        help_text = """
Blackjack Rules:

- Goal: Get closer to 21 than the dealer without going over.
- Cards: Number cards are face value, face cards (J,Q,K) are 10, Aces are 11 or 1.
- Betting: Place your bet, then deal.
- Actions:
  - Hit: Take another card.
  - Stand: Keep your current hand.
  - Double Down: Double your bet, take one card, then stand (only on first two cards).
- Dealer: Must hit until 17 or higher.
- Blackjack: Ace + 10-value card on first two cards pays 3:2.
- Win: Higher value than dealer, or dealer busts.
- Lose: Go over 21, or lower value than dealer.
- Push: Tie.

Good luck!
        """
        messagebox.showinfo("Blackjack Help", help_text)

def main():
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()