import tkinter as tk
from PIL import Image, ImageTk

# Import our game classes
from game1_tictactoe import TicTacToeGame
from game2_guessnumber import GuessNumberGame
from game3_multiplication import MultiplicationGame

class GameManager:
    """
    Main controller for the Best-of-3 series.
    Tracks scores, manages shared images, and switches between games.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("BO3 Showdown")
        self.root.geometry("500x500")

        # --- SHARED DATA ---
        self.p1_wins = 0
        self.p2_wins = 0
        self.current_game_index = 0
        self.last_round_winner = None # To know if we can proceed

        # Register games here - easy to add game4, game5, etc.
        self.game_list = [
            TicTacToeGame,
            GuessNumberGame,
            MultiplicationGame
        ]

        # Load shared images once (using Pillow)
        self.x_img = ImageTk.PhotoImage(Image.open("x.png").resize((100, 100)))
        self.o_img = ImageTk.PhotoImage(Image.open("o.png").resize((100, 100)))
        self.empty_img = ImageTk.PhotoImage(Image.open("empty.png").resize((100, 100)))

        # Create a container frame where games will place their widgets
        self.game_container = tk.Frame(self.root)
        self.game_container.pack(expand=True, fill="both")

        # Global Score Label
        self.score_label = tk.Label(self.root, text="", font=("Arial", 12), fg="darkgreen")
        self.score_label.pack(side="bottom", pady=10)

        # Bind the 'N' key for proceeding to the next game
        self.root.bind("<n>", self.handle_next_key)
        self.root.bind("<N>", self.handle_next_key)

        # Start the first game
        self.start_game()

    def update_score_display(self):
        self.score_label.config(text=f"Series Score: Player 1 ({self.p1_wins}) - Player 2 ({self.p2_wins})")

    def start_game(self):
        """
        Clears the current game and loads the next one in the list.
        """
        # 1. Clear previous widgets
        for widget in self.game_container.winfo_children():
            widget.destroy()

        self.update_score_display()
        self.last_round_winner = None # Reset for the new round

        # 2. Check if series is already won
        if self.p1_wins == 2:
            self.show_series_winner("Player 1")
            return
        if self.p2_wins == 2:
            self.show_series_winner("Player 2")
            return

        # 3. Check if we ran out of games
        if self.current_game_index >= len(self.game_list):
            if self.p1_wins > self.p2_wins:
                self.show_series_winner("Player 1")
            elif self.p2_wins > self.p1_wins:
                self.show_series_winner("Player 2")
            else:
                self.show_series_winner("It's a Draw")
            return

        # 4. Initialize the next game class
        game_class = self.game_list[self.current_game_index]
        self.current_active_game = game_class(self.game_container, self)

    def report_winner(self, winner_name):
        """
        Called by individual games to report who won that round.
        """
        self.last_round_winner = winner_name
        if winner_name == "Player 1":
            self.p1_wins += 1
        elif winner_name == "Player 2":
            self.p2_wins += 1
        
        self.update_score_display()

    def handle_next_key(self, event):
        """
        Moves to the next game if the current round is over.
        """
        if self.last_round_winner is not None:
            self.current_game_index += 1
            self.start_game()

    def show_series_winner(self, winner_name):
        """
        Final screen when the Best-of-3 is complete.
        """
        for widget in self.game_container.winfo_children():
            widget.destroy()
        
        tk.Label(self.game_container, text="🏆 SERIES COMPLETE 🏆", font=("Arial", 24, "bold"), fg="gold").pack(pady=30)
        
        result_text = f"Champion: {winner_name}\n\nFinal Score:\nPlayer 1: {self.p1_wins}\nPlayer 2: {self.p2_wins}"
        tk.Label(self.game_container, text=result_text, font=("Arial", 18)).pack(pady=20)
        
        tk.Button(self.game_container, text="Play Again", font=("Arial", 14), bg="green", fg="white", 
                  command=self.reset_series).pack(pady=10)

    def reset_series(self):
        """
        Restarts the entire series from scratch.
        """
        self.p1_wins = 0
        self.p2_wins = 0
        self.current_game_index = 0
        self.start_game()
