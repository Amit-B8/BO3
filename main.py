import tkinter as tk
from game_manager import GameManager

def main():
    """
    Main entry point for the BO3 Showdown application.
    """
    # 1. Create the base window
    root = tk.Tk()
    
    # 2. Start the Game Manager (this handles everything)
    GameManager(root)
    
    # 3. Keep the window open
    root.mainloop()

# This part ensures the game only runs if this file is executed directly
if __name__ == "__main__":
    main()
