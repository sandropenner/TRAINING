import tkinter 
from tkinter import ttk

root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
root.title("Calculator")
root.geometry("500x200")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10), background="blue", foreground="black")
style.configure("TRadiobutton", font=("Arial", 10))

calc_entry = ttk.Entry(root, font=("Arial", 10))
calc_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button1 = ttk.Button(root, text="1")
button1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
