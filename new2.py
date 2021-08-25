import tkinter as tk    
from tkinter import ttk

root =  tk.Tk()
root.geometry("240x100")
root.title("login")

root.columnconfigure(0,weight = 1)
root.columnconfigure(1, weight = 3)

username_label = ttk.Label(root, text = "Username: ")
username_label.grid(column=0,row=0,padx = 5, pady= 5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1,row=0,padx = 5, pady= 5)

passWord_label = ttk.Label(root, text = "PWD: ")
passWord_label.grid(column=0,row=1,padx = 5, pady= 5)

passWord_entry = ttk.Entry(root)
passWord_entry.grid(column=1,row=1,padx = 5, pady= 5)

login_button = ttk.Button(root,text = "Login")
login_button.grid(column=2,row=3,padx = 5, pady= 5)

root.mainloop()