import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

# Lớp Tooltip cho các Widget
class ToolTip:
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.tooltip = None

    def show_tooltip(self, event):
        if self.tooltip or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
        self.tooltip = None


# Lớp App chính
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI")
        self.root.geometry("450x250")
        self.root.resizable(False, False)

        self.create_menu()
        self.create_tabs()

    # Tạo MenuBar
    def create_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_app)

        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both")

        # Tab 1
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Tab 1")
        self.create_tab1(tab1)
        ToolTip(tab1, "Hello Gui")
        # Tab 2
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Tab 2")
        self.create_tab2(tab2)
        ToolTip(tab2, "Hello Gui")
    # Tạo nội dung cho Tab 1
    def create_tab1(self, tab):
        main_frame = ttk.LabelFrame(tab, text="Mighty Python")
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

        button1 = tk.Button(frame1, text="Click Me!", font=("Arial", 10), command=lambda: self.on_button_click(entry1, combo))
        button1.grid(row=1, column=2)

        spinbox = tk.Spinbox(frame1, values=(1, 2, 4, 42, 100), width=5, font=("Arial", 12), bd = 10)
        spinbox.grid(row=2, column=0, padx=5, pady=10)
        ToolTip(spinbox, "This is spinbox")

        ToolTip(button1, "Nhấn nút này để chào hỏi!")

    # Tạo nội dung cho Tab 2
    def create_tab2(self, tab):
        frame2 = ttk.LabelFrame(tab, text="The Snake")
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
        radio_blue = ttk.Radiobutton(frame2, text="Blue", variable=color_var, value="Blue", command=lambda: self.on_color_change(color_var))
        radio_blue.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        radio_gold = ttk.Radiobutton(frame2, text="Gold", variable=color_var, value="Gold", command=lambda: self.on_color_change(color_var))
        radio_gold.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        radio_red = ttk.Radiobutton(frame2, text="Red", variable=color_var, value="Red", command=lambda: self.on_color_change(color_var))
        radio_red.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Frame sẽ thay đổi màu nền
        self.frame4 = tk.LabelFrame(frame2, text="Labels in a Frame", bg="light blue")
        self.frame4.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        label_inside1 = tk.Label(self.frame4, text="Label1", bg="light blue")
        label_inside1.grid(row=0, column=0, padx=5)

        label_inside2 = tk.Label(self.frame4, text="Label2", bg="light blue")
        label_inside2.grid(row=0, column=1, padx=5)

        label_inside3 = tk.Label(self.frame4, text="Label3", bg="light blue")
        label_inside3.grid(row=0, column=2, padx=5)

    # Sự kiện khi nhấn nút
    def on_button_click(self, entry, combo):
        name = entry.get()
        number = combo.get()
        messagebox.showinfo("Thông báo", f"Hello {name} {number}")

    # Thay đổi màu nền
    def on_color_change(self, color_var):
        selected_color = color_var.get().lower()
        self.frame4.config(bg=selected_color)

    # Hiển thị thông tin About
    def show_about(self):
        messagebox.showinfo("About", "This is a Python GUI created using Tkinter.")

    # Tạo file mới
    def new_file(self):
        messagebox.showinfo("New File", "New File selected")

    # Thoát ứng dụng
    def exit_app(self):
        self.root.quit()


# Khởi tạo ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
