from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    wn.after_cancel(timer)
    checks_label.config(text="")
    text_label.config(text="Timer", fg=GREEN)
    Canvas.itemconfig(canvas, tagOrId=timer_text, text="00:00")
    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    shrot_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8==0:
        text_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
       
    elif reps%2==0:
        text_label.config(text="Break", fg=PINK)
        count_down(shrot_break_sec)
    else: 
        text_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count>=0:
        Canvas.itemconfig(canvas ,tagOrId= timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = wn.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+= "✔"
        checks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

wn = Tk()
wn.title("pomodoro")
wn.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
directory = "tom.png"
tomato_img = PhotoImage(file=directory)

text_label = Label(text="Timer", fg=GREEN,
bg=YELLOW, font=(FONT_NAME, 30, "bold"))

canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))


checks_label = Label(text="", fg=GREEN,
bg=YELLOW, font=(FONT_NAME, 15, "normal"))

start_btn = Button(text="start",bg="white", highlightthickness=0, command=start_timer)
reset_btn = Button(text="reset",bg="white", highlightthickness=0, command=reset)

text_label.grid(row=1, column=2)
canvas.grid(row=2, column=2)
start_btn.grid(row=3, column=1)
reset_btn.grid(row=3, column=3)
checks_label.grid(row=4, column=2)



wn.mainloop()