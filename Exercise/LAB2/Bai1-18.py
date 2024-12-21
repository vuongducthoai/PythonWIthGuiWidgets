import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

root = tk.Tk()
root.title("Python GUI")
root.geometry("450x400")
root.resizable(False, False)

def on_button_click1():
    name1 = entry1.get()
    name2 = combo.get()
    button1.config(text=f"Hello {name1} {name2}")

def on_color_change():
    selected_color = color_var.get()
    root.config(bg=selected_color.lower())

def new_file():
    messagebox.showinfo("New File", "New File selected")

def exit_app():
    root.quit()

def show_about():
    messagebox.showinfo("About", "This is a Python GUI created using Tkinter.")

#Add the MenuBar
menubar = tk.Menu(root)

#Creating the "File menu"
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=exit_app)

#Add "File" to the Menubar
menubar.add_cascade(label="File", menu=filemenu)


# Create the "Help" menu
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)

# Add "Help" to the MenuBar
menubar.add_cascade(label="Help", menu=helpmenu)

#Display the Menubar
root.config(menu=menubar)

style = ttk.Style()
style.configure("Custom.TLabelframe.Label", foreground="blue")

main_frame = ttk.LabelFrame(root, text="Mighty Python", style="Custom.TLabelframe")
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

frame1 = ttk.Frame(main_frame)
frame1.grid(row=0, column=0, padx=5, pady=5, sticky="ew", columnspan=3)

label1 = tk.Label(frame1, text="Enter a name:", font=("Arial, 12"))
label1.grid(row=0, column=0, pady=5, sticky="w")

entry1 = tk.Entry(frame1, font=("Arial", 12))
entry1.grid(row=1, column=0)
entry1.focus_set()

label2 = tk.Label(frame1, text="Choose a number:", font=("Arial, 12"))
label2.grid(row=0, column=1, pady=5)

combo = ttk.Combobox(frame1, values=["42", "1", "2", "42", "100"])
combo.grid(row=1, column=1)

button1 = tk.Button(frame1, text="Click Me!", font=("Arial", 10), command=on_button_click1)
button1.grid(row=1, column=2)


frame2 = ttk.Frame(main_frame)
frame2.grid(row=1, column=0, padx=5, pady=5, sticky="ew", columnspan=3)

var1 = tk.IntVar(value=1)
check1 = ttk.Checkbutton(frame2, text="Disabled", variable=var1, state="disabled")
check1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

var2 = tk.IntVar(value=0)
check2 = ttk.Checkbutton(frame2, text="UnChecked", variable=var2)
check2.grid(row=0, column=1, padx=10, pady=5, sticky="w")

var3 = tk.IntVar(value=1)
check3 = ttk.Checkbutton(frame2, text="Enabled", variable=var3)
check3.grid(row=0, column=2, padx=10, pady=5, sticky="w")

frame3 = ttk.Frame(main_frame)
frame3.grid(row=2, column=0, padx=5, pady=5, sticky="ew", columnspan=3)

scrolled_text = scrolledtext.ScrolledText(frame3, wrap=tk.WORD, width=30, height=5, font=("Arial", 12))
scrolled_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

color_var = tk.StringVar(value="Blue")
radio_blue = ttk.Radiobutton(frame3, text="Blue", variable=color_var, value="Blue", command=on_color_change)
radio_blue.grid(row=1, column=0, padx=10, pady=5, sticky="w")

radio_gold = ttk.Radiobutton(frame3, text="Gold", variable=color_var, value="Gold", command=on_color_change)
radio_gold.grid(row=1, column=1, padx=10, pady=5, sticky="w")

radio_red = ttk.Radiobutton(frame3, text="Red", variable=color_var, value="Red", command=on_color_change)
radio_red.grid(row=1, column=2, padx=10, pady=5, sticky="w")




frame4 = ttk.LabelFrame(main_frame, text="Labels in a Frame", style="Custom.TLabelframe")
frame4.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

label_inside1 = tk.Label(frame4, text="Label1")
label_inside1.grid(row=0, column=0, padx=5)

label_inside2 = tk.Label(frame4, text="Label2")
label_inside2.grid(row=0, column=1, padx=5)

label_inside3 = tk.Label(frame4, text="Label3")
label_inside3.grid(row=0, column=2, padx=5)

root.mainloop()
