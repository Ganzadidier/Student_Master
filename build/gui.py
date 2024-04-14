from random import random, shuffle
from pathlib import Path
import json
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Label, LEFT, RIGHT, Toplevel

USER_DATA_FILE = "user_data_file.json"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Student_Master\build\assets\frame0")
global window 


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_question():
    
    global question, answer, answers, true_answers

    verbal_questions = {
        "The sum of any two odd numbers is even.": True,
        "Every prime number greater than 2 can be written as the sum of two prime numbers.": False,
        "A triangle can have more than one right angle.": False,
        "All squares are rectangles.": True,
        "An obtuse angle is greater than a right angle.": True,
        "A prime number can be negative.": False,
        "The square root of any positive number is real.": True,
        "All rational numbers are integers.": False,
        "Two parallel lines intersect at only one point.": False,
        "A quadrilateral can have all sides of equal length.": False
    }

    all_questions = list(verbal_questions.keys())
    shuffle(all_questions)
    question = all_questions.pop()
    
    answer = verbal_questions[question]

    answers.append(answer)
    true_answers.append(answer)
    label.config(text=question)



def check_answer(user_answer):
    global score, question_index, label, true_button, false_button, answers, true_answers

    if user_answer == true_answers[question_index]:
        score += 1
    question_index += 1
    if question_index < 10:
        generate_question()
    else:
        show_score()




def show_score():
    global score
    score_window = Toplevel(window)
    score_window.title("Quiz Score")

    score_label = Label(score_window, text=f"Your score: {score}/10", font=("Helvetica", 24))
    score_label.pack()



def second_page():
    window_1 = Tk()
    window_1.title("Home Page of Quizler App")
    window_1.geometry("659x492")
    window_1.configure(bg = "#F0EBEB")


    canvas = Canvas(
        window_1,
        bg = "#F0EBEB",
        height = 492,
        width = 659,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    def math_page():
        if window_1.winfo_viewable():
            window_1.destroy()
        
        global window, score, question_index, questions, answers, label, true_button, false_button, true_answers
        window = Tk()
        window.title("Math Quiz")
        window.geometry("659x492")
        window.configure(bg = "#F0EBEB")
        canvas = Canvas(
            window,
            bg = "#F0EBEB",
            height = 492,
            width = 659,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        math_label = Label(text="Welcome to math Quiz", font=("Arial", 24, "bold"))
        math_label.pack()
        
        
        
        score = 0
        question_index = 0
        answers = []
        true_answers = []
        label = Label(window, text="", wraplength=300, font=("Helvetica", 12))
        label.pack()
        true_button = Button(window, text="True", command=lambda: check_answer(True))
        true_button.pack(side=LEFT, padx=20)
        false_button = Button(window, text="False", command=lambda: check_answer(False))
        false_button.pack(side=RIGHT, padx=20)
        
        
        generate_question()
        
        
        
        
        
        window.minsize(False, False)
        window.mainloop()

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )

    button_1.place(
        x=371.0,
        y=121.0,
        width=199.0,
        height=135.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=math_page,
        relief="flat"
    )

    button_2.place(
        x=52.0,
        y=121.0,
        width=236.9864959716797,
        height=135.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )


    button_3.place(
        x=353.0,
        y=291.0,
        width=236.9864959716797,
        height=144.0
    )


    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))


    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )

    button_4.place(
        x=69.0,
        y=291.0,
        width=196.0,
        height=144.0
    )

    category_image_4 = PhotoImage(
        file=relative_to_assets("image_1.png"))

    category_button = Button(
        image=category_image_4,
        borderwidth=0,
        relief="flat"
    )
    category_button.place(
        x=70,
        y=50.0
    )

    imigongo_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png")
    )

    imigongo_button = Button(
        image=imigongo_image_2,
        borderwidth=0,
        relief="flat"
    )


    imigongo_button.place(
        x=642,
        y=10
    )


    window_1.resizable(False, False)
    window_1.mainloop()



def load_users():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save users to the JSON file


def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)


def sign_up():
    users = load_users()
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        if username in users:
            messagebox.showwarning("Warning", "User already exists\n kindly sign in.")
        else:
            users[username] = password
            save_users(users)
            messagebox.showinfo("Success", "You have successfully registered.\n "
                                           "Please go back and sign in to enjoy our services.")

    else:
        messagebox.showerror("Error", "Unknown Error")


def sign_in():
    users = load_users()
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        if window.winfo_viewable():
            window.destroy()
            second_page()
        else:
            second_page()
    else:
        messagebox.showerror("Error", "Invalid username or password.")


window = Tk()

window.geometry("659x492")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 492,
    width = 659,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    301.0,
    492.0,
    fill="#002333",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("green_separator.png"))
image_1 = canvas.create_image(
    91.0,
    231.0,
    image=image_image_1
)

canvas.create_text(
    31.0,
    137.99999973739898,
    anchor="nw",
    text="Welcome Back\nto Student Master🎓",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)

canvas.create_text(
    35.0,
    262.0,
    anchor="nw",
    text="Sign up to continue to your account",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    489.5,
    169.5,
    image=entry_image_1
)
password_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
password_entry.place(
    x=391.0,
    y=145.0,
    width=197.0,
    height=51.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    489.5,
    288.5,
    image=entry_image_2
)
username_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
username_entry.place(
    x=391.0,
    y=264.0,
    width=197.0,
    height=51.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("Signin.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sign_in,
    relief="flat"
)
button_1.place(
    x=510.0,
    y=351.0,
    width=103.0,
    height=40.272727966308594
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Signup.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up,
    relief="flat"
)
button_2.place(
    x=364.0,
    y=351.0,
    width=105.0,
    height=40.0
)

canvas.create_text(
    376.0,
    114.0,
    anchor="nw",
    text="Enter your Email:",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    376.0,
    228.0,
    anchor="nw",
    text="Enter your Password:",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
