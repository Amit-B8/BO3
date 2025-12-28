# 🏆 BO3 Showdown

**BO3 Showdown** is a Python-based desktop game designed to simulate a "Best of 3" match. Built using Python and Tkinter, it features a graphical user interface (GUI) to track scores and determine the winner.

## 🌟 Features
* **Best of 3 Logic:** Automatically tracks wins and declares a champion when a player reaches 2 wins.
* **Graphical Interface:** Visual display using Python's `tkinter` library.
* **Image Support:** Uses `Pillow` (PIL) to render images/graphics for the game state.
* **Reset Functionality:** Easily restart the match without closing the application.

## 🛠️ Prerequisites
Before running the game, ensure you have Python installed on your machine.
* [Download Python](https://www.python.org/downloads/) (Version 3.10 or higher recommended)

## 🚀 Installation & Setup

Follow these steps to set up the project locally:

1.  **Navigate to the project folder:**
    ```bash
    cd path/to/BO3Showdown
    ```

2.  **Create a Virtual Environment:**
    (This keeps your project dependencies isolated)
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Environment:**
    * **Windows (PowerShell):**
        ```powershell
        .\.venv\Scripts\Activate
        ```
    * **Mac/Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install Dependencies:**
    This project requires `Pillow` for image handling.
    ```bash
    pip install pillow
    ```

## 🎮 How to Run
Once your environment is set up and active (you should see `(.venv)` in your terminal), run the game:

```bash
python main.py