import tkinter as tk

root = tk.Tk()

#1
root.title("Python GUI")

root.geometry("400x300")

#2
root.resizable(False, False) 

#4
def on_button_click1():
    label1.config(text="A red Label", fg="red")
    button1.config(text="** I have been Clicked! **")


#3
label1 = tk.Label(root, text="A Label", font=("Arial", 12))
label1.grid(row=0, column=0)

button1 = tk.Button(root, text="Click Me!", font=("Arial", 10), command=on_button_click1)
button1.grid(row=0, column = 1)

root.mainloop()
