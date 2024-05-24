import tkinter as tk
import random

# Function to determine the result of the game
def determine_winner(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
        scores['draws'] += 1
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        scores['wins'] += 1
    else:
        result = "You lose!"
        scores['losses'] += 1

    # Update the result label
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    # Update the scores
    update_scores()

# Function to update the scores displayed on the GUI
def update_scores():
    score_label.config(text=f"Wins: {scores['wins']}  Losses: {scores['losses']}  Draws: {scores['draws']}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")

# Initialize scores
scores = {'wins': 0, 'losses': 0, 'draws': 0}

# Create a label for the title
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=('Helvetica', 18, 'bold'))
title_label.pack(pady=10)

# Create buttons for Rock, Paper, Scissors
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=('Helvetica', 14), width=10, command=lambda: determine_winner('rock'))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=('Helvetica', 14), width=10, command=lambda: determine_winner('paper'))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=('Helvetica', 14), width=10, command=lambda: determine_winner('scissors'))
scissors_button.grid(row=0, column=2, padx=5)

# Create a label to display the result
result_label = tk.Label(root, text="", font=('Helvetica', 14), fg="blue")
result_label.pack(pady=20)

# Create a label to display the scores
score_label = tk.Label(root, text="Wins: 0  Losses: 0  Draws: 0", font=('Helvetica', 14), fg="green")
score_label.pack(pady=10)

# Run the application
root.mainloop()


