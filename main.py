import tkinter as tk
import tkinter.messagebox as messagebox
import random
import time
from PIL import Image, ImageTk

# First, create the root window
root = tk.Tk()
root.title("Tic Tac Toe - BO3 Showdown")

# Track scores and series state (initial setup only)
player1Score = 0
player2Score = 0
player1Wins = 0
player2Wins = 0
games_played = 0

# Load images (after creating root)
x_img = ImageTk.PhotoImage(Image.open("x.png").resize((100, 100)))
o_img = ImageTk.PhotoImage(Image.open("o.png").resize((100, 100)))
empty_img = ImageTk.PhotoImage(Image.open("empty.png").resize((100, 100)))

current_player = "X"
board_state = [["" for _ in range(3)] for _ in range(3)]
buttons = []

status_label = tk.Label(root, text="", font=("Arial", 16), fg="green")
status_label.grid(row=3, column=0, columnspan=3)
score_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
score_label.grid(row=4, column=0, columnspan=3)
series_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
series_label.grid(row=5, column=0, columnspan=3)


# Function to handle a player's move
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
        elif check_tie():
            end_game("It's a tie!")
        else:
            current_player = "O" if current_player == "X" else "X"

        show_scores()

# Function to check win conditions
def check_win(player):
    for i in range(3):
        if all(board_state[i][j] == player for j in range(3)):
            return True
        if all(board_state[j][i] == player for j in range(3)):
            return True
    if all(board_state[i][i] == player for i in range(3)):
        return True
    if all(board_state[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check for a tie
def check_tie():
    return all(board_state[i][j] != "" for i in range(3) for j in range(3))

# Function to end the game (disable buttons and show message)
def end_game(message):
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")
    status_label.config(text=message + " Press 'N' to start the next game.")

# Function to show current scores
def show_scores():
    score_label.config(text=f"Player 1 Score: {player1Score} | Player 2 Score: {player2Score}")

# Function to proceed to next game on pressing 'n'
def next_game(event=None):
    global board_state, current_player, games_played
    games_played += 1
    current_player = "X"
    board_state = [["" for _ in range(3)] for _ in range(3)]
    status_label.config(text="New game started! Player X goes first.")

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(image=empty_img, state="normal")

    # Placeholder for second game function call
    if games_played == 2:
        second_game_placeholder()
    elif games_played == 3:
        third_game_placeholder()

def second_game_placeholder():
    global secret_num, current_player, guess_entry, guess_button, guess_feedback_label

    # Hide the Tic Tac Toe buttons
    for row in buttons:
        for btn in row:
            btn.grid_remove()

    # Determine who lost Game 1
    if player1Score > player2Score:
        current_player = "O"  # Player 2 lost
    elif player2Score > player1Score:
        current_player = "X"  # Player 1 lost
    else:
        current_player = "X"  # Tie fallback

    # Set up game instructions
    status_label.config(text=f"Game 2: Guess the number between 1 and 20! Player {current_player} goes first.")

    secret_num = random.randint(1, 20)

    # Entry box for guess input
    guess_entry = tk.Entry(root, font=("Arial", 14))
    guess_entry.grid(row=6, column=0, columnspan=200, sticky="we", padx=10, pady=10)
    guess_entry.focus()

    # Submit button
    guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=process_guess)
    guess_button.grid(row=6, column=2, padx=10, pady=10)

    # Feedback label
    guess_feedback_label = tk.Label(root, text="", font=("Arial", 14), fg="purple")
    guess_feedback_label.grid(row=7, column=0, columnspan=3)

    # Shrink window size for Game 2 layout
    root.geometry("400x250")

def process_guess():
    global current_player
    guess_str = guess_entry.get()
    if not guess_str.isdigit():
        guess_feedback_label.config(text="Please enter a valid number!")
        guess_entry.delete(0, tk.END)
        return

    guess = int(guess_str)
    if guess < 1 or guess > 20:
        guess_feedback_label.config(text="Number must be between 1 and 20.")
        guess_entry.delete(0, tk.END)
        return

    if guess == secret_num:
        guess_feedback_label.config(
            text=f"Player {current_player} guessed {guess} and WINS! Secret was {secret_num}. Press 'N' for next game.")
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")
    else:
        guess_feedback_label.config(text=f"Player {current_player} guessed {guess}. Wrong! Next player's turn.")
        current_player = "O" if current_player == "X" else "X"
        guess_entry.delete(0, tk.END)


def third_game_placeholder():
    global current_player, mult_entry, mult_button, mult_feedback_label, timer_id
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.grid_remove()
    root.geometry("400x250")
    
    # Create widgets for the multiplication game
    mult_question_label.config(text="")
    mult_question_label.grid(row=6, column=0, columnspan=3, pady=5)
    
    mult_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="we")
    mult_entry.focus()
    mult_button.grid(row=7, column=2, padx=10, pady=5)
    mult_feedback_label.grid(row=8, column=0, columnspan=3)
    
    next_mult_turn()

def next_mult_turn():
    global current_player, MultNum1, MultNum2, product, start_time, timer_id
    
    MultNum1 = random.randint(1, 9)
    MultNum2 = random.randint(10, 99)
    product = MultNum1 * MultNum2
    mult_question_label.config(text=f"Player {current_player}: What is {MultNum1} x {MultNum2}? (5s)")
    
    mult_entry.config(state="normal")
    mult_button.config(state="normal")
    mult_entry.delete(0, tk.END)
    start_time = time.time()
    
    # Cancel previous timer if exists
    if timer_id:
        root.after_cancel(timer_id)
    
    # Start a 5-second timeout
    timer_id = root.after(5000, handle_timeout)

def process_mult_guess():
    global current_player, timer_id
    elapsed = time.time() - start_time
    guess_str = mult_entry.get()
    
    if timer_id:
        root.after_cancel(timer_id)
    
    if not guess_str.isdigit():
        mult_feedback_label.config(text="Please enter a valid number!")
        return

    guess = int(guess_str)
    if elapsed > 5:
        mult_feedback_label.config(text=f"Player {current_player} ran out of time! Player {'O' if current_player == 'X' else 'X'} WINS!")
        end_mult_game()
    elif guess == product:
        mult_feedback_label.config(text=f"Correct! Now it's the other player's turn.")
        current_player = "O" if current_player == "X" else "X"
        root.after(1000, next_mult_turn)
    else:
        mult_feedback_label.config(text=f"Wrong! The correct answer was {product}. Player {'O' if current_player == 'X' else 'X'} WINS!")
        end_mult_game()

# Multiplication game widgets
mult_question_label = tk.Label(root, text="", font=("Arial", 16), fg="black")
mult_entry = tk.Entry(root, font=("Arial", 14))
mult_button = tk.Button(root, text="Submit", font=("Arial", 14), command=process_mult_guess)
mult_feedback_label = tk.Label(root, text="", font=("Arial", 14), fg="purple")

timer_id = None
start_time = 0

def handle_timeout():
    mult_feedback_label.config(text=f"Time’s up! Player {current_player} took too long. Player {'O' if current_player == 'X' else 'X'} WINS!")
    end_mult_game()

def end_mult_game():
    mult_entry.config(state="disabled")
    mult_button.config(state="disabled")
    status_label.config(text="Game 3 Over. Press 'N' to restart series.")


# Bind keys for 'n' to proceed to next game
root.bind("n", next_game)
root.bind("N", next_game)

# Create the Tic Tac Toe board
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, image=empty_img, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Start the first game automatically
next_game()

root.mainloop()
