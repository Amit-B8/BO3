import tkinter as tk

class TicTacToeGame:
    """
    Class for the Tic-Tac-Toe game.
    """
    def __init__(self, container, manager):
        self.container = container
        self.manager = manager  # Reference to GameManager for scoring/images
        
        # Game State
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.game_active = True

        # Build UI
        self.setup_ui()

    def setup_ui(self):
        # Status Label to show whose turn it is
        self.status_label = tk.Label(self.container, text="Tic Tac Toe: Player X (P1) Turn", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create 3x3 grid of buttons
        for i in range(3):
            row_btns = []
            for j in range(3):
                # Use empty image from manager
                btn = tk.Button(self.container, image=self.manager.empty_img, 
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i+1, column=j)
                row_btns.append(btn)
            self.buttons.append(row_btns)

    def on_click(self, r, c):
        # Only allow click if game is active and spot is empty
        if not self.game_active or self.board[r][c] != "":
            return

        btn = self.buttons[r][c]
        if self.current_player == "X":
            btn.config(image=self.manager.x_img)
            self.board[r][c] = "X"
        else:
            btn.config(image=self.manager.o_img)
            self.board[r][c] = "O"

        # Check for win or tie
        if self.check_win(self.current_player):
            winner_name = "Player 1" if self.current_player == "X" else "Player 2"
            self.status_label.config(text=f"{winner_name} Wins! Press 'N' for next game.", fg="blue")
            self.game_active = False
            self.manager.report_winner(winner_name) # Tell manager who won
        elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            self.status_label.config(text="Tie! No points. Press 'N' for next game.", fg="orange")
            self.game_active = False
            self.manager.report_winner("Draw")
        else:
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            p_tag = "P1" if self.current_player == "X" else "P2"
            self.status_label.config(text=f"Tic Tac Toe: Player {self.current_player} ({p_tag}) Turn")

    def check_win(self, p):
        b = self.board
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(b[i][j] == p for j in range(3)): return True
            if all(b[j][i] == p for j in range(3)): return True
        if b[0][0] == p and b[1][1] == p and b[2][2] == p: return True
        if b[0][2] == p and b[1][1] == p and b[2][0] == p: return True
        return False
