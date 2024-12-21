import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tooltip_window or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True) 
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(tw, text=self.text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10))
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
        self.tooltip_window = None

root = tk.Tk()
root.title("Python GUI")
root.geometry("450x500")
root.resizable(False, False)

def on_button_click1():
    name1 = entry1.get()
    name2 = combo.get()
    button1.config(text=f"Hello {name1} {name2}")

def on_color_change():
    selected_color = color_var.get().lower()
    frame4.config(bg=selected_color)

def new_file():
    messagebox.showinfo("New File", "New File selected")

def exit_app():
    root.quit()

def show_about():
    messagebox.showinfo("This is a Title", "Python GUI created using tkinter: The year is 2022")

def on_spinbox_change():
    value = spinbox.get()
    scrolled_text.insert(tk.END, f"{value}\n") 
    scrolled_text.yview(tk.END)  
def run_progressbar():
    progress.start(10)

def stop_progressbar():
    progress.stop()

def reset_progressbar():
    progress.stop()
    progress['value'] = 0

def increase_by_one():
    current_value = progress['value']
    progress['value'] = current_value + 10

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_app)

menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)

menubar.add_cascade(label="Help", menu=helpmenu)

# Display the MenuBar
root.config(menu=menubar)

# Create a Notebook (for Tabs)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Tab1 Frame
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")

# Tab2 Frame
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Tab 3")

# ================== Content for Tab 1 ===================
main_frame = ttk.LabelFrame(tab1, text="Mighty Python")
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

# Spinbox with values and callback
spinbox = tk.Spinbox(frame1, values=(1, 2, 4, 42, 100), width=5, font=("Arial", 12), command=on_spinbox_change, bd = 10)
spinbox.grid(row=2, column=0, padx=5)


spinbox = tk.Spinbox(frame1, values=(1, 2, 4, 42, 100), width=5, font=("Arial", 12), command=on_spinbox_change, bd = 10, relief="raised")
spinbox.grid(row=2, column=1, padx=5)

scrolled_text = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=30, height=5, font=("Arial", 12))
scrolled_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
ToolTip(scrolled_text, "This is a ScrolledText widget")

# ================== Content for Tab 2 ===================
frame2 = ttk.LabelFrame(tab2, text="The Snake")
frame2.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

var1 = tk.IntVar(value=1)
check1 = ttk.Checkbutton(frame2, text="Disabled", variable=var1, state="disabled")
check1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

var2 = tk.IntVar(value=0)
check2 = ttk.Checkbutton(frame2, text="UnChecked", variable=var2)
check2.grid(row=0, column=1, padx=10, pady=5, sticky="w")

var3 = tk.IntVar(value=1)
check3 = ttk.Checkbutton(frame2, text="Enabled", variable=var3)
check3.grid(row=0, column=2, padx=10, pady=5, sticky="w")

color_var = tk.StringVar(value="Blue")
radio_blue = ttk.Radiobutton(frame2, text="Blue", variable=color_var, value="Blue", command=on_color_change)
radio_blue.grid(row=1, column=0, padx=10, pady=5, sticky="w")

radio_gold = ttk.Radiobutton(frame2, text="Gold", variable=color_var, value="Gold", command=on_color_change)
radio_gold.grid(row=1, column=1, padx=10, pady=5, sticky="w")

radio_red = ttk.Radiobutton(frame2, text="Red", variable=color_var, value="Red", command=on_color_change)
radio_red.grid(row=1, column=2, padx=10, pady=5, sticky="w")


# LabelFrame that will change color
frame4 = tk.LabelFrame(frame2, text="ProgressBar", bg="light blue")
frame4.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

btn_run  = tk.Button(frame4, text="Run Progressbar", bg="light blue", command=run_progressbar)
btn_run.grid(row=0, column=0, padx=5)

btn_start  = tk.Button(frame4, text="Start Progressbar", bg="light blue", command=increase_by_one)
btn_start.grid(row=1, column=0, padx=5)

btn_stop   = tk.Button(frame4, text="Stop immediately", bg="light blue", command=stop_progressbar)
btn_stop.grid(row=2, column=0, padx=5)

btn_reset = tk.Button(frame4, text="Stop after second",bg="light blue", command=reset_progressbar)
btn_reset.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

progress = ttk.Progressbar(frame2, orient='horizontal', length=300, mode='determinate')
progress.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

ToolTip(progress, "This is a progress bar")
# ================== Content for Tab 3 ===================
canvas = tk.Canvas(tab3, width=400, height=200)
canvas.grid(row=0, column=0, padx=10, pady=10)

canvas.create_rectangle(0, 0, 200, 100, fill="orange")  # top - left - bottom - right
canvas.create_rectangle(200, 0, 400, 100, fill="blue")  
canvas.create_rectangle(0, 100, 200, 200, fill="blue") 
canvas.create_rectangle(200, 100, 400, 200, fill="orange")  

root.mainloop()
