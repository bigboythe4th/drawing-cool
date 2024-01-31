import tkinter as tk
import random
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# start variables
score, current_question, correct_answer, difficulty, time_limit, question_number = 0, "", "", "easy", 20, 0
math_coins, correct_answers_count, incorrect_answers_count = 0, 0, 0

# Questions and answers database
easy_questions = ["What is 5 + 3?", "What is 7 * 4?", "What is 12 / 3?", "What is 16 / 2?", "What is 1 + 3?"]
easy_answers = ["8", "28", "4" , "8", "4"]

medium_questions = ["What is 15 - 7?", "What is 6 * 9?", "What is 25 / 5?", "What is 245 + 543?"]
medium_answers = ["8", "54", "5", "788"]

hard_questions = ["What is the square root of 144?", "What is 12^3?", "What is 10! (factorial)?", "What is 2^9?",]
hard_answers = ["12", "1728", "3628800","512"]

# Function to start a new quiz 
def start_quiz(selected_difficulty):
    global score, current_question, correct_answer, difficulty, time_limit, question_number, correct_answers_count, incorrect_answers_count
    score, difficulty, question_number, correct_answers_count, incorrect_answers_count = 0, selected_difficulty, 0, 0, 0
    select_question()
    update_score()
    update_math_coins()
    start_timer()

# Function to start a new quiz question
def select_question():
    global current_question, correct_answer
    questions, answers = easy_questions, easy_answers if difficulty == "easy" else (medium_questions, medium_answers if difficulty == "medium" else hard_questions, hard_answers)
    current_question = random.choice(questions)
    correct_answer = answers[questions.index(current_question)]
    question_label.config(text=current_question)

# Function to check the user's answer and earn MathCoins
def check_answer():
    global score, question_number, math_coins, correct_answers_count, incorrect_answers_count
    user_answer = entry_answer.get()
    if user_answer == correct_answer:
        feedback_label.config(text="Correct!", fg="green")
        score += 1
        math_coins += 5
        correct_answers_count += 1
    else:
        feedback_label.config(text="Incorrect. Correct answer: " + correct_answer, fg="red")
        incorrect_answers_count += 1

    question_number += 1
    if question_number < 5:
        select_question()
        update_score()
        entry_answer.delete(0, tk.END)
        plot_bar_graph()
    else:
        end_quiz()

# Function to end the quiz and show earned MathCoins
def end_quiz():
    global timer
    if timer:
        root.after_cancel(timer)
    messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour Score: {score}\nMathCoins Earned: {math_coins}")
    entry_answer.config(state="disabled")
    submit_button.config(state="disabled")
    start_button.config(state="normal")

# Function to update the players score
def update_score():
    score_label.config(text="Score: " + str(score))

# Function to update MathCoins screan
def update_math_coins():
    math_coins_label.config(text="MathCoins: " + str(math_coins))

# Function to start the timer
def start_timer():
    global time_limit, timer
    time_left = tk.StringVar()
    time_left.set(time_limit)
    timer_label.config(textvariable=time_left)

    def countdown():
        global time_limit
        if time_limit > 0:
            time_limit -= 1
            time_left.set(time_limit)
            timer = root.after(1000, countdown)
        else:
            end_quiz()

    countdown()

# Function to change the difficulty level
def change_difficulty():
    global difficulty
    difficulty = difficulty_var.get()
    select_question()
    difficulty_label.config(text="Selected Difficulty: " + difficulty.capitalize())

# Function to show a bar graph showing correct and incorrect answers
def plot_bar_graph():
    global ax, canvas
    labels, counts, colors = ["Correct", "Incorrect"], [correct_answers_count, incorrect_answers_count], ['green', 'red']

    # Clear the last graph
    ax.clear()
    ax.bar(labels, counts, color=colors)
    ax.set_xlabel("Answer Status")
    ax.set_ylabel("Count")
    ax.set_title("Quiz Performance")
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Math Tycoon Game")

# Set the window size
window_width, window_height = 800, 600
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
x_coordinate, y_coordinate = (screen_width - window_width) // 2, (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create GUI 
question_label = tk.Label(root, text="", font=("Arial", 24))
entry_answer = tk.Entry(root, font=("Arial", 20))
submit_button = tk.Button(root, text="Submit Answer", command=check_answer, font=("Arial", 18))
feedback_label = tk.Label(root, text="", fg="black", font=("Arial", 18))
score_label = tk.Label(root, text="Score: 0", font=("Arial", 20))
timer_label = tk.Label(root, text="Time Left: 0", font=("Arial", 20))
start_button = tk.Button(root, text="Start Quiz", command=lambda: start_quiz(difficulty_var.get()), font=("Arial", 18))
difficulty_var = tk.StringVar(value="easy")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "easy", "medium", "hard")
change_difficulty_button = tk.Button(root, text="Change Difficulty", command=change_difficulty, font=("Arial", 18))
math_coins_label = tk.Label(root, text="MathCoins: 0", font=("Arial", 20))

# Add parts to the GUI
difficulty_label = tk.Label(root, text="Selected Difficulty: Easy", font=("Arial", 20))
difficulty_menu.config(font=("Arial", 18))
difficulty_menu.pack()
change_difficulty_button.pack()
difficulty_label.pack()
start_button.pack()
score_label.pack()
math_coins_label.pack()
timer_label.pack()
question_label.pack(pady=20)
entry_answer.pack()
submit_button.pack()
feedback_label.pack()

# Create a separate window for the bar graph
graph_window = tk.Toplevel(root)
graph_window.title("Quiz Performance")
graph_window.geometry("400x400")

# Create a Figure and an axis for the bar graph
fig, ax = plt.subplots(figsize=(4, 4))
canvas = FigureCanvasTkAgg(fig, master=graph_window)
canvas.get_tk_widget().pack()
canvas.draw()

# Start the Tkinter event loop
root.mainloop()



