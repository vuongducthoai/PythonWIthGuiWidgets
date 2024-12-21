import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

root = tk.Tk()

#1
root.title("Python GUI")

root.geometry("400x300")

#2
root.resizable(False, False) 

def on_spinbox_change():
    value = spinbox.get()
    scrolled_text.insert(tk.END, f"{value}\n") 
    scrolled_text.yview(tk.END)  


spinbox = tk.Spinbox(root, values=(1, 2, 4, 42, 100), width=5, font=("Arial", 12), command=on_spinbox_change, bd = 10)
spinbox.grid(row=0, column=0, padx=5)


scrolled_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=5, font=("Arial", 12))
scrolled_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

root.mainloop()