import tkinter as tk

root = tk.Tk()


root.title("Python GUI")

root.geometry("400x300")

root.resizable(False, False) 

def on_button_click1():
    name = entry1.get() #Lay du lieu tu o nhap lieu
    button1.config(text=f"Hello {name}")


label1 = tk.Label(root, text="Enter a name:", font=("Arial, 12"))
label1.grid(row = 0,column=0,pady=5, sticky="w")

entry1 = tk.Entry(root, font=("Arial", 12))
entry1.grid(row = 1, column=0)

entry1.focus_set()

button1 = tk.Button(root, text="Click Me!", font=("Arial", 10), command=on_button_click1, state='disabled')
button1.grid(row=1, column=1)

root.mainloop()
