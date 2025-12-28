import tkinter as tk
import random
from tkinter import messagebox
import game1 

# Main Application Class
class BO3Showdown:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("BO3 Showdown - Main Menu")
        self.show_main_menu()

    def show_main_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.root.geometry("400x300")
        
        # Title
        title = tk.Label(self.root, text="BO3 Showdown", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        # Option A: Pick Game
        btn_pick = tk.Button(self.root, text="Option A: Pick a Game", 
                             font=("Arial", 14), width=20, 
                             command=self.show_pick_menu)
        btn_pick.pack(pady=10)

        # Option B: Random Game
        btn_random = tk.Button(self.root, text="Option B: Random Game", 
                               font=("Arial", 14), width=20, 
                               command=self.start_random_game)
        btn_random.pack(pady=10)

        # Exit
        btn_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        btn_exit.pack(pady=20)

    def show_pick_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select a Game", font=("Arial", 20)).pack(pady=20)

        # Button for Game 1
        btn_g1 = tk.Button(self.root, text="1. Tic Tac Toe", 
                           font=("Arial", 14), width=20,
                           command=lambda: self.launch_game(1))
        btn_g1.pack(pady=5)

        # Placeholders for future games
        btn_g2 = tk.Button(self.root, text="2. Number Guess (Coming Soon)", 
                           font=("Arial", 14), width=20, state="disabled")
        btn_g2.pack(pady=5)

        btn_g3 = tk.Button(self.root, text="3. Multiplication (Coming Soon)", 
                           font=("Arial", 14), width=20, state="disabled")
        btn_g3.pack(pady=5)

        # Back Button
        btn_back = tk.Button(self.root, text="Back", command=self.show_main_menu)
        btn_back.pack(pady=20)

    def start_random_game(self):
        # Logic to pick random number 1-3
        # Since only Game 1 exists, we force 1 for now
        game_choice = 1  
        messagebox.showinfo("Random Pick", f"Randomly selected: Game {game_choice}")
        self.launch_game(game_choice)

    def launch_game(self, game_id):
        if game_id == 1:
            # CALL GAME 1 HERE
            # We pass 'self.show_main_menu' so Game 1 knows how to return
            game1.run(self.root, self.show_main_menu)
        else:
            print("Game not implemented yet")

# App Start
if __name__ == "__main__":
    root = tk.Tk()
    app = BO3Showdown(root)
    root.mainloop()