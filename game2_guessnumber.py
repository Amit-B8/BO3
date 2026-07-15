import tkinter as tk
import random

class GuessNumberGame:
    """
    Class for the Number Guessing game (Closest Guess).
    Both players enter a guess, and the person closest to the secret number wins.
    """
    def __init__(self, container, manager):
        self.container = container
        self.manager = manager
        
        # Secret number between 1 and 20
        self.secret_num = random.randint(1, 20)
        self.game_active = True

        self.setup_ui()

    def setup_ui(self):
        # Instructions
        tk.Label(self.container, text="Round 2: Closest Guess Wins!", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.container, text="I'm thinking of a number between 1 and 20.\nBoth players guess. Whoever is closer wins!", 
                 font=("Arial", 12)).pack(pady=5)

        # Player 1 Input
        tk.Label(self.container, text="Player 1 Guess:", font=("Arial", 10, "bold"), fg="blue").pack(pady=(10, 0))
        self.p1_entry = tk.Entry(self.container, font=("Arial", 14))
        self.p1_entry.pack(pady=5)
        self.p1_entry.focus() # Start focus here

        # Player 2 Input
        tk.Label(self.container, text="Player 2 Guess:", font=("Arial", 10, "bold"), fg="red").pack(pady=(10, 0))
        self.p2_entry = tk.Entry(self.container, font=("Arial", 14))
        self.p2_entry.pack(pady=5)

        # Bind Enter key to submit (on both entries)
        self.p1_entry.bind("<Return>", lambda e: self.check_result())
        self.p2_entry.bind("<Return>", lambda e: self.check_result())

        # Submit Button
        self.submit_btn = tk.Button(self.container, text="Submit Guesses", font=("Arial", 12), 
                                    bg="lightgray", command=self.check_result)
        self.submit_btn.pack(pady=20)
        
        # Feedback Label
        self.feedback_label = tk.Label(self.container, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

    def check_result(self):
        if not self.game_active:
            return

        try:
            # Get values
            p1_val = int(self.p1_entry.get())
            p2_val = int(self.p2_entry.get())

            # Calculate distance
            p1_diff = abs(p1_val - self.secret_num)
            p2_diff = abs(p2_val - self.secret_num)

            result_text = f"Secret Number was {self.secret_num}!\n"
            result_text += f"P1: {p1_val} (Off by {p1_diff})\n"
            result_text += f"P2: {p2_val} (Off by {p2_diff})\n\n"

            winner_name = ""

            if p1_diff < p2_diff:
                result_text += "Player 1 Wins Round!"
                color = "blue"
                winner_name = "Player 1"
            elif p2_diff < p1_diff:
                result_text += "Player 2 Wins Round!"
                color = "red"
                winner_name = "Player 2"
            else:
                result_text += "It's a Tie!"
                color = "orange"
                winner_name = "Draw"

            # Show result and end game
            self.feedback_label.config(text=result_text + "\nPress 'N' for next game.", fg=color)
            self.game_active = False
            self.p1_entry.config(state="disabled")
            self.p2_entry.config(state="disabled")
            self.submit_btn.config(state="disabled")
            
            # Report to manager
            self.manager.report_winner(winner_name)

        except ValueError:
            self.feedback_label.config(text="Please enter valid numbers!", fg="red")
