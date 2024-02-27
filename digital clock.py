# A digital clock is an alternative to a traditional analogue clock.This type of clock shows numbers to display the time in a digital format.
from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font=("Boulder",68,'bold')
background = "green"
foreground = "orange"
border_widht = 25

label = Label(app_window,font=text_font, bg=background, fg=foreground, bd=border_widht)
label.grid(row=0, column=1)

def deigital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, deigital_clock)

deigital_clock()
app_window.mainloop()