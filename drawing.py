import tkinter as tk
import random
import tkinter.font as tkFont
from tkinter import messagebox
import time  # Required for timer

# Initialize variables
score = 0
current_question = ""
correct_answer = ""
difficulty = "easy"  # Default difficulty
time_limit = 20  # Default time limit in seconds
timer = None
question_number = 0
math_coins = 0  # Introduce virtual currency

# Define upgrades and their properties
upgrades = [
    {"name": "Upgrade 1", "cost": 50, "effect": 10},
    {"name": "Upgrade 2", "cost": 100, "effect": 20},
    {"name": "Upgrade 3", "cost": 150, "effect": 30}
]

# Questions and answers database (for easy, medium, and hard levels)
easy_questions = [
    "What is 5 + 3?",
    "What is 7 * 4?",
    "What is 12 / 3?"
]

easy_answers = ["8", "28", "4"]

medium_questions = [
    "What is 15 - 7?",
    "What is 6 * 9?",
    "What is 25 / 5?"
]

medium_answers = ["8", "54", "5"]

hard_questions = [
    "What is the square root of 144?",
    "What is 12^3?",
    "What is 10! (factorial)?"
]

hard_answers = ["12", "1728", "3628800"]

# Function to initialize a new quiz session
def start_quiz(selected_difficulty):
    global score, current_question, correct_answer, difficulty, time_limit, question_number
    score = 0
    difficulty = selected_difficulty
    question_number = 0
    select_question()
    update_score()
    update_math_coins()  # Initialize MathCoins display
    update_progress()
    start_timer()

# Function to start a new quiz question
def select_question():
    global current_question, correct_answer
    if difficulty == "easy":
        current_question = random.choice(easy_questions)
        correct_answer = easy_answers[easy_questions.index(current_question)]
    elif difficulty == "medium":
        current_question = random.choice(medium_questions)
        correct_answer = medium_answers[medium_questions.index(current_question)]
    elif difficulty == "hard":
        current_question = random.choice(hard_questions)
        correct_answer = hard_answers[hard_questions.index(current_question)]
    question_label.config(text=current_question)

# Function to check the user's answer and earn MathCoins
def check_answer():
    global score, question_number, math_coins
    user_answer = entry_answer.get()
    if user_answer == correct_answer:
        feedback_label.config(text="Correct!", fg="green")
        score += 1
        # Reward MathCoins for correct answers
        math_coins += 5  # Adjust the amount as needed
        update_score()
        update_math_coins()
    else:
        feedback_label.config(text="Incorrect. Correct answer: " + correct_answer, fg="red")

    question_number += 1
    if question_number < 5:  # Adjust the number of questions per quiz
        select_question()
        update_score()
        entry_answer.delete(0, tk.END)
    else:
        end_quiz()

# Function to end the quiz and display earned MathCoins
def end_quiz():
    global timer
    if timer:
        root.after_cancel(timer)
    messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour Score: {score}\nMathCoins Earned: {math_coins}")
    entry_answer.config(state="disabled")
    submit_button.config(state="disabled")
    start_button.config(state="normal")
    leaderboard_button.config(state="normal")
    hints_button.config(state="normal")

# Function to update the player's score
def update_score():
    score_label.config(text="Score: " + str(score))

# Function to update MathCoins display
def update_math_coins():
    math_coins_label.config(text="MathCoins: " + str(math_coins))

# Function to start the timer

# Function to provide a hint
def give_hint():
    hint_text = ""
    if difficulty == "easy":
        hint_text = "Hint: It's a basic arithmetic operation."
    elif difficulty == "medium":
        hint_text = "Hint: It's a multiplication problem."
    elif difficulty == "hard":
        hint_text = "Hint: It's a mathematical function involving factorials."

    messagebox.showinfo("Hint", hint_text)

# Function to buy upgrades
def buy_upgrade():
    global math_coins, score
    selected_upgrade = random.choice(upgrades)  # Select a random upgrade
    upgrade_cost = selected_upgrade["cost"]
    upgrade_effect = selected_upgrade["effect"]

    if math_coins >= upgrade_cost:
        math_coins -= upgrade_cost
        score += upgrade_effect  # Apply the upgrade's effect
        update_score()
        update_math_coins()
        messagebox.showinfo("Upgrade Purchased", f"Purchased {selected_upgrade['name']} for {upgrade_cost} MathCoins.")
    else:
        messagebox.showerror("Insufficient MathCoins", "You don't have enough MathCoins to purchase this upgrade.")

# Function to change the difficulty level
def change_difficulty():
    global difficulty
    difficulty = difficulty_var.get()
    select_question()
    difficulty_label.config(text="Selected Difficulty: " + difficulty.capitalize())

# Create the main window
root = tk.Tk()
root.title("Math Tycoon Game")

# Set the window size


# Create GUI components with adjusted fonts and positions


# Create a font object for the difficulty menu
menu_font = tkFont.Font(family="Arial", size=18)

# Create the difficulty menu


# Create a button to change difficulty
change_difficulty_button = tk.Button(root, text="Change Difficulty", command=change_difficulty, font=("Arial", 18))
change_difficulty_button.pack()

# Initialize MathCoins label
math_coins_label = tk.Label(root, text="MathCoins: 0", font=("Arial", 20))

# Add the components to the GUI
difficulty_label.pack()
start_button.pack()
score_label.pack()
math_coins_label.pack()  # Display MathCoins
timer_label.pack()
question_label.pack(pady=20)
entry_answer.pack()
submit_button.pack()
hints_button.pack()
feedback_label.pack()
leaderboard_button.pack()

# Load sound files for correct and incorrect answers
# Place "correct.wav" and "incorrect.wav" in the same directory as your script

# Start the Tkinter event loop
root.mainloop()