from tkinter import * 
from tkinter import ttk


def frame1(parent):
    frame_1 = ttk.Frame(parent)
    # frame_1.columnconfigure(0,weight = 1)
    # frame_1.columnconfigure(0 , weight = 3)
    button_frame1 = ttk.Button(frame_1,text="test1")
    button_frame1.grid(row = 2, column = 2, sticky = W)    
    button_frame2 = ttk.Button(frame_1,text="test2")
    button_frame2.grid(row = 3, column = 2, sticky = E)
    button_frame3 = ttk.Button(frame_1,text="test3")
    button_frame3.grid(column=0,row=2)
    button_frame4 = ttk.Button(frame_1,text="test4")
    button_frame4.grid(column=0,row=3)
    button_frame9 = ttk.Button(button_frame1,text="test9")
    button_frame9.grid(column=0,row=0)    
    return frame_1


def frame2(parent):
    frame_2 = ttk.Frame(parent)
    # frame_2.columnconfigure(0,weight = 1)
    # frame_2.columnconfigure(0 , weight = 3)
    button_frame1 = ttk.Button(frame_2,text="test5")
    button_frame1.grid(column=0,row=0)    
    button_frame2 = ttk.Button(frame_2,text="test6")
    button_frame2.grid(column=0,row=1)
    button_frame3 = ttk.Button(frame_2,text="test7")
    button_frame3.grid(column=0,row=2)
    button_frame4 = ttk.Button(frame_2,text="test8")
    button_frame4.grid(column=0,row=3)
    return frame_2

def main_window():
    root = Tk()
    root.geometry("440x500")
    root.title("Test Frame")
    root.columnconfigure(0,weight = 5)
    root.columnconfigure(1,weight = 1)

    input_frame1 = frame1(root)
    input_frame1.grid(column=0,row=0 )
    input_frame2 = frame2(root)
    input_frame2.grid(column=1,row=0 )
    
    root.mainloop()
if __name__ == "__main__":
    main_window()