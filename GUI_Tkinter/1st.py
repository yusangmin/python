import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, solumnspan=3)

name_entered.focus()

win.mainloop()