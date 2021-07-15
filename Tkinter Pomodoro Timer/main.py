## Pomodoro Work Timer

import time
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO = "tomato.png"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_action():
    print("Reset button pressed")
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text="")
    label.config(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_action():
    print("Start button pressed")
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # long break
    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", font=(FONT_NAME, 35), bg=YELLOW, fg=RED)
    # work countdowns
    elif reps % 2 != 0:
        countdown(work_sec)
        label.config(text="Work", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
    # short break
    else:
        countdown(short_break_sec)
        label.config(text="Break", font=(FONT_NAME, 35), bg=YELLOW, fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_button_action()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer text
label = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

# tomato and clock
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=TOMATO)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)


# Start button
start_button = Button(text="Start", command=start_button_action, highlightthickness=0, font=(FONT_NAME, 8))
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", command=reset_button_action, highlightthickness=0, font=(FONT_NAME, 8))
reset_button.grid(column=2, row=2)


# check mark
check_marks = Label(font=('bold'), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
