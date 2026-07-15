import tkinter as tk
import random
import time

class MultiplicationGame:
    """
    Class for the Multiplication game.
    Players take turns solving a problem within 5 seconds.
    """
    def __init__(self, container, manager):
        self.container = container
        self.manager = manager
        
        # Game State
        self.current_player = "X" # X is P1, O is P2
        self.game_active = True
        self.timer_id = None
        self.start_time = 0
        self.product = 0

        self.setup_ui()
        self.next_turn()

    def setup_ui(self):
        tk.Label(self.container, text="Round 3: Multiplication Challenge", font=("Arial", 16, "bold")).pack(pady=10)
        
        self.question_label = tk.Label(self.container, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.container, font=("Arial", 14))
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", lambda e: self.check_answer())

        self.submit_btn = tk.Button(self.container, text="Submit", font=("Arial", 12), command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.feedback_label = tk.Label(self.container, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

    def next_turn(self):
        if not self.game_active:
            return

        # Generate problem
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        self.product = num1 * num2
        
        p_name = "Player 1" if self.current_player == "X" else "Player 2"
        self.question_label.config(text=f"{p_name}: What is {num1} x {num2}? (5s)")
        
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()
        self.start_time = time.time()

        # Cancel old timer and start new 5s timer
        if self.timer_id:
            self.container.after_cancel(self.timer_id)
        self.timer_id = self.container.after(5000, self.handle_timeout)

    def check_answer(self):
        if not self.game_active:
            return

        # Cancel timer immediately on submit
        if self.timer_id:
            self.container.after_cancel(self.timer_id)

        guess_str = self.answer_entry.get()
        if not guess_str.isdigit():
            self.feedback_label.config(text="Please enter a number!", fg="red")
            self.next_turn() # Give them another chance or just restart turn? 
            return

        guess = int(guess_str)
        if guess == self.product:
            # Correct! Now it's the other player's turn
            self.feedback_label.config(text="Correct! Next player's turn...", fg="green")
            self.current_player = "O" if self.current_player == "X" else "X"
            self.container.after(1000, self.next_turn)
        else:
            # Wrong answer - game ends
            winner_name = "Player 2" if self.current_player == "X" else "Player 1"
            self.end_game(f"Wrong! {self.product} was the answer. {winner_name} Wins Round!", winner_name)

    def handle_timeout(self):
        winner_name = "Player 2" if self.current_player == "X" else "Player 1"
        self.end_game(f"Time's up! {winner_name} Wins Round!", winner_name)

    def end_game(self, message, winner_name):
        self.game_active = False
        self.question_label.config(text="Game Over")
        self.feedback_label.config(text=message + "\nPress 'N' for series results.", fg="red")
        self.answer_entry.config(state="disabled")
        self.submit_btn.config(state="disabled")
        
        # Report to manager
        self.manager.report_winner(winner_name)
