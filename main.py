import tkinter as tk
from PIL import Image, ImageTk

# First, create the root window
root = tk.Tk()
root.title("Tic Tac Toe - BO3 Showdown")

player1Score = 0
player2Score = 0

# Then load your images (after creating root)
x_img = ImageTk.PhotoImage(Image.open("x.png").resize((100, 100)))
o_img = ImageTk.PhotoImage(Image.open("o.png").resize((100, 100)))
empty_img = ImageTk.PhotoImage(Image.open("empty.png").resize((100, 100)))

current_player = "X"
board_state = [["" for _ in range(3)] for _ in range(3)]
buttons = []

def on_click(row, col):
    global current_player, player1Score, player2Score
    btn = buttons[row][col]
    if btn['image'] == str(empty_img) and board_state[row][col] == "":
        if current_player == "X":
            btn.config(image=x_img)
            board_state[row][col] = "X"
        else:
            btn.config(image=o_img)
            board_state[row][col] = "O"

        if check_win(current_player):
            if current_player == "X":
                player1Score += 1
            else:
                player2Score += 1
            end_game(f"{current_player} wins!")
            show_scores()
        elif check_tie():
            end_game("It's a tie!")
            show_scores()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_win(player):
    for i in range(3):
        if all(board_state[i][j] == player for j in range(3)):  # Row
            return True
        if all(board_state[j][i] == player for j in range(3)):  # Column
            return True
    if all(board_state[i][i] == player for i in range(3)):  # Diagonal
        return True
    if all(board_state[i][2 - i] == player for i in range(3)):  # Other diagonal
        return True
    return False

def check_tie():
    return all(board_state[i][j] != "" for i in range(3) for j in range(3))

def end_game(message):
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")
    tk.Label(root, text=message, font=("Arial", 16), fg="green").grid(row=3, column=0, columnspan=3)

def show_scores():
    score_text = f"Player 1 Score: {player1Score} | Player 2 Score: {player2Score}"
    tk.Label(root, text=score_text, font=("Arial", 14), fg="blue").grid(row=4, column=0, columnspan=3)



# This part will create the board
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, image=empty_img, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

root.mainloop()
