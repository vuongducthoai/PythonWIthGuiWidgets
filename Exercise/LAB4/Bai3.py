import tkinter as tk

GLOBAL_CONST = 42

def create_gui():
    win = tk.Tk()
    win.title("Simple GUI")

    label = tk.Label(win, text="Enter your name:")
    label.grid(row=0, column=0)

    name_entered = tk.Entry(win)
    name_entered.grid(row=0, column=1)

    print(GLOBAL_CONST)

    name_entered.focus()

    win.mainloop()

    
create_gui()
print('GLOBAL_CONST:', GLOBAL_CONST)

