import tkinter as tk

#Create instance of tkinter
win = tk.Tk()

#Create DoubleVar
strData = tk.StringVar()

strData.set("Hello StringVar")

varData = strData.get()

#Print out current value of strData
print(varData)


intData = tk.IntVar()
print(intData)
print(intData.get())