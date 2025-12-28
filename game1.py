import tkinter as tk
import random
from PIL import Image, ImageTk

class Game1Gauntlet:
    def __init__(self, root, on_back_to_menu):
        self.root = root
        self.on_back_to_menu = on_back_to_menu
        
        # --- SCORE TRACKING ---
        self.p1_wins = 0
        self.p2_wins = 0
        self.current_round = 1

        # Load Images
        self.x_img = ImageTk.PhotoImage(Image.open("x.png").resize((100, 100)))
        self.o_img = ImageTk.PhotoImage(Image.open("o.png").resize((100, 100)))
        self.empty_img = ImageTk.PhotoImage(Image.open("empty.png").resize((100, 100)))

        # Start the series
        self.run_tictactoe()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- SERIES LOGIC ---
    def add_win(self, winner):
        # Update Scores
        if winner == "Player 1":
            self.p1_wins += 1
        elif winner == "Player 2":
            self.p2_wins += 1
        
        # Check for Series Win (Best of 3)
        if self.p1_wins == 2:
            self.show_series_winner("Player 1")
        elif self.p2_wins == 2:
            self.show_series_winner("Player 2")
        elif self.current_round == 3:
            # If round 3 ends and nobody has 2 wins (e.g. 1-1-1 tie), decide by points
            if self.p1_wins > self.p2_wins:
                self.show_series_winner("Player 1")
            elif self.p2_wins > self.p1_wins:
                self.show_series_winner("Player 2")
            else:
                self.show_series_winner("It's a Draw")
        else:
            # Series continues -> Go to next game
            self.current_round += 1
            if self.current_round == 2:
                self.root.after(2000, self.run_number_guess)
            elif self.current_round == 3:
                self.root.after(2000, self.run_rps)

    def show_series_winner(self, winner_name):
        self.clear_screen()
        self.root.title("Series Over")
        
        tk.Label(self.root, text="🏆 SERIES COMPLETE 🏆", font=("Arial", 20, "bold"), fg="gold").pack(pady=30)
        
        result_text = f"Winner: {winner_name}\n\nFinal Score:\nPlayer 1: {self.p1_wins}\nPlayer 2: {self.p2_wins}"
        tk.Label(self.root, text=result_text, font=("Arial", 16)).pack(pady=20)
        
        tk.Button(self.root, text="Back to Main Menu", bg="green", fg="white", font=("Arial", 14),
                  command=self.on_back_to_menu).pack(pady=20)

    # ==========================================
    # ROUND 1: TIC TAC TOE (PvP)
    # ==========================================
    def run_tictactoe(self):
        self.clear_screen()
        self.root.title("Round 1: Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.game_active = True

        # Show current score at top
        score_text = f"Score: P1 ({self.p1_wins}) - P2 ({self.p2_wins})"
        tk.Label(self.root, text=score_text, font=("Arial", 12), fg="gray").grid(row=0, column=0, columnspan=3)
        
        self.status_label = tk.Label(self.root, text="Tic Tac Toe: Player X (P1) Turn", font=("Arial", 14))
        self.status_label.grid(row=1, column=0, columnspan=3, pady=10)

        for i in range(3):
            row_btns = []
            for j in range(3):
                btn = tk.Button(self.root, image=self.empty_img, 
                                command=lambda r=i, c=j: self.on_ttt_click(r, c))
                btn.grid(row=i+2, column=j)
                row_btns.append(btn)
            self.buttons.append(row_btns)

    def on_ttt_click(self, r, c):
        if not self.game_active or self.board[r][c] != "":
            return

        btn = self.buttons[r][c]
        if self.current_player == "X":
            btn.config(image=self.x_img)
            self.board[r][c] = "X"
        else:
            btn.config(image=self.o_img)
            self.board[r][c] = "O"

        if self.check_ttt_win(self.current_player):
            winner = "Player 1" if self.current_player == "X" else "Player 2"
            self.status_label.config(text=f"{winner} Wins Round 1!", fg="blue")
            self.game_active = False
            self.add_win(winner)
        elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            self.status_label.config(text="Tie! No points awarded.", fg="orange")
            self.game_active = False
            self.add_win("Draw") 
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            p_name = "P1" if self.current_player == "X" else "P2"
            self.status_label.config(text=f"Tic Tac Toe: Player {self.current_player} ({p_name}) Turn")

    def check_ttt_win(self, p):
        b = self.board
        for i in range(3):
            if all(b[i][j] == p for j in range(3)): return True
            if all(b[j][i] == p for j in range(3)): return True
        if b[0][0] == p and b[1][1] == p and b[2][2] == p: return True
        if b[0][2] == p and b[1][1] == p and b[2][0] == p: return True
        return False

    # ==========================================
    # ROUND 2: NUMBER GUESS (P1 vs P2)
    # ==========================================
    # ==========================================
    # ROUND 2: NUMBER GUESS (Closest Wins)
    # ==========================================
    def run_number_guess(self):
        self.clear_screen()
        self.root.title("Round 2: Closest Guess")
        
        # 1. Generate the secret number (1-20)
        self.secret_num = random.randint(1, 20)

        # Show Score at the top
        tk.Label(self.root, text=f"Score: P1 ({self.p1_wins}) - P2 ({self.p2_wins})", font=("Arial", 12), fg="gray").pack()
        
        tk.Label(self.root, text="Round 2: Closest Guess Wins!", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"I am thinking of a number between 1 and 20.\nBoth players guess. Whoever is closer wins!", font=("Arial", 12)).pack(pady=5)

        # --- Player 1 Input ---
        tk.Label(self.root, text="Player 1 Guess:", font=("Arial", 10, "bold"), fg="blue").pack(pady=(10, 0))
        self.p1_entry = tk.Entry(self.root, font=("Arial", 14))
        self.p1_entry.pack(pady=5)

        # --- Player 2 Input ---
        tk.Label(self.root, text="Player 2 Guess:", font=("Arial", 10, "bold"), fg="red").pack(pady=(10, 0))
        self.p2_entry = tk.Entry(self.root, font=("Arial", 14))
        self.p2_entry.pack(pady=5)

        # Submit Button
        tk.Button(self.root, text="Submit Both Guesses", font=("Arial", 12), bg="lightgray", 
                  command=self.check_closest_guess).pack(pady=20)
        
        # Feedback Label
        self.guess_feedback = tk.Label(self.root, text="", font=("Arial", 12))
        self.guess_feedback.pack(pady=10)

    def check_closest_guess(self):
        try:
            # 1. Get inputs
            p1_val = int(self.p1_entry.get())
            p2_val = int(self.p2_entry.get())

            # 2. Calculate distances from secret number
            p1_diff = abs(p1_val - self.secret_num)
            p2_diff = abs(p2_val - self.secret_num)

            result_text = f"Secret Number was {self.secret_num}!\n"
            result_text += f"P1 Guessed: {p1_val} (Off by {p1_diff})\n"
            result_text += f"P2 Guessed: {p2_val} (Off by {p2_diff})\n\n"

            winner = ""

            # 3. Determine Winner
            if p1_diff < p2_diff:
                result_text += "Player 1 is closer! P1 Wins Round."
                self.guess_feedback.config(text=result_text, fg="blue")
                winner = "Player 1"
            elif p2_diff < p1_diff:
                result_text += "Player 2 is closer! P2 Wins Round."
                self.guess_feedback.config(text=result_text, fg="red")
                winner = "Player 2"
            else:
                result_text += "It's a Tie! No points awarded."
                self.guess_feedback.config(text=result_text, fg="orange")
                winner = "Draw"

            # 4. Disable inputs so they can't submit again
            self.p1_entry.config(state="disabled")
            self.p2_entry.config(state="disabled")

            # 5. Move to next round after delay
            self.root.after(3000, lambda: self.add_win(winner))

        except ValueError:
            self.guess_feedback.config(text="Please enter valid numbers for both players!", fg="red")

    # ==========================================
    # ROUND 3: ROCK PAPER SCISSORS (P1 vs P2/CPU)
    # ==========================================
    def run_rps(self):
        self.clear_screen()
        self.root.title("Round 3: Rock Paper Scissors")

        # Show Score
        tk.Label(self.root, text=f"Score: P1 ({self.p1_wins}) - P2 ({self.p2_wins})", font=("Arial", 12), fg="gray").pack()
        
        tk.Label(self.root, text="Round 3: Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Player 1 vs Computer (representing Player 2)", font=("Arial", 12)).pack(pady=5)
        
        self.rps_result_label = tk.Label(self.root, text="Choose your weapon!", font=("Arial", 14))
        self.rps_result_label.pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        for choice in ["Rock", "Paper", "Scissors"]:
            tk.Button(btn_frame, text=choice, font=("Arial", 12), width=10,
                      command=lambda c=choice: self.play_rps(c)).pack(side="left", padx=5)

    def play_rps(self, player_choice):
        options = ["Rock", "Paper", "Scissors"]
        comp_choice = random.choice(options) # Computer acts as Player 2
        
        outcome = ""
        winner = ""
        
        if player_choice == comp_choice:
            outcome = "It's a Tie!"
            winner = "Draw"
        elif (player_choice == "Rock" and comp_choice == "Scissors") or \
             (player_choice == "Paper" and comp_choice == "Rock") or \
             (player_choice == "Scissors" and comp_choice == "Paper"):
            outcome = "Player 1 Wins!"
            winner = "Player 1"
        else:
            outcome = "Player 2 (Computer) Wins!"
            winner = "Player 2"

        self.rps_result_label.config(text=f"P2 Chose: {comp_choice}\n{outcome}", fg="blue")
        
        # Disable buttons so they can't play twice
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    btn.config(state="disabled")

        # Delay slightly so they can read the result before series ends
        self.root.after(1500, lambda: self.add_win(winner))

# Entry point called by main.py
def run(root, on_back_callback):
    Game1Gauntlet(root, on_back_callback)