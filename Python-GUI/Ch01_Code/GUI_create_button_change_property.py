#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("파이썬 GUI")   

# Adding a Label that will get modified
a_label = ttk.Label(win, text="라벨")
a_label.grid(column=0, row=0)

# Button Click Event Function
def click_me():
    action.configure(text="** 클릭했어! **")
    a_label.configure(foreground='red')
    a_label.configure(text='빨간색 라벨')

# Adding a Button
action = ttk.Button(win, text="클릭!", command=click_me)   
action.grid(column=1, row=0)

#======================
# Start GUI
#======================
win.mainloop()