import tkinter as tk
from tkinter import ttk
from tkinter import * 

def create_main_window():

    root = tk.Tk()
    root.title('Replace')
    root.geometry('600x400')
    root.resizable(0, 0)
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)
    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)
    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)
    root.mainloop()


def create_input_frame(root):
    createFrame = ttk.Frame(root)
    createFrame.columnconfigure(0, weight=1)
    createFrame.columnconfigure(0, weight=3)
    ttk.Label(createFrame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(createFrame, width=30)
    keyword.grid(column=1, row=0, sticky=tk.W)
    ttk.Label(createFrame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(createFrame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)
    return createFrame

def create_button_frame(root):
    buttonFrame = ttk.Frame(root)
    buttonFrame.columnconfigure(0, weight=1)
    ttk.Button(buttonFrame, text='Find Next').grid(column=0, row=0)
    ttk.Button(buttonFrame, text='Replace').grid(column=0, row=1)
    ttk.Button(buttonFrame, text='Replace All').grid(column=0, row=2)
    ttk.Button(buttonFrame, text='Cancel',command = root.destroy).grid(column=0, row=3)
    return buttonFrame

if __name__ == "__main__":
    create_main_window()
