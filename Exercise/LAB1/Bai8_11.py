import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()


root.title("Python GUI")

root.geometry("430x200")

root.resizable(False, False) 

def on_button_click1():
    name1 = entry1.get() 
    name2 = combo.get()
    button1.config(text=f"Hello {name1} {name2}")


def on_color_change():
    selected_color = color_var.get()
    root.config(bg=selected_color.lower()) 

label1 = tk.Label(root, text="Enter a name:", font=("Arial, 12"))
label1.grid(row = 0,column=0,pady=5, sticky="w")

entry1 = tk.Entry(root, font=("Arial", 12))
entry1.grid(row = 1, column=0)
entry1.focus_set()

label2 = tk.Label(root, text="Choose a number:", font=("Arial, 12"))
label2.grid(row = 0,column=1,pady=5, )

combo = ttk.Combobox(root, values=["42", "1", "2", "42", "100"])
combo.grid(row = 1, column = 1)

button1 = tk.Button(root, text="Click Me!", font=("Arial", 10), command=on_button_click1)
button1.grid(row=1, column=2)


var1 = tk.IntVar(value=1)
check1 = ttk.Checkbutton(root, text="Disabled", variable=var1, state="disabled", )
check1.grid(row=2, column=0, padx=10, pady=5, sticky="w")

var2 = tk.IntVar(value=0)
check2 = ttk.Checkbutton(root, text="UnChecked", variable=var2)
check2.grid(row=2, column=1, padx=10, pady=5, sticky="w")

var3 = tk.IntVar(value=1)
check3 = ttk.Checkbutton(root, text="Enabled", variable=var3)
check3.grid(row=2, column=2, padx=10, pady=5, sticky="w")


color_var = tk.StringVar(value="Blue")
radio_blue = ttk.Radiobutton(root, text="Blue", variable=color_var, value="Blue", command=on_color_change)
radio_blue.grid(row=3, column=0, padx=10, pady=5, sticky="w")

radio_gold = ttk.Radiobutton(root, text="Gold", variable=color_var, value="Gold", command=on_color_change)
radio_gold.grid(row=3, column=1, padx=10, pady=5, sticky="w")

radio_red = ttk.Radiobutton(root, text="Red", variable=color_var, value="Red", command=on_color_change)
radio_red.grid(row=3, column=2, padx=10, pady=5, sticky="w")


scrolled_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=5, font=("Arial", 12))
scrolled_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

root.mainloop() 