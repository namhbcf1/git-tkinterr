from tkinter import *
from tkinter import ttk


master = Tk()
master.geometry('300x200')  

pane = Frame(master)
pane.pack(fill=BOTH,expand=True)
style = ttk.Style()
style.configure("lm1.TButton", background = "red")
b1 = ttk.Button(pane,text= "click me!", style= "lm1.TButton")
b1.pack(ipadx=10,ipady=10,side = TOP, fill="x")

b2 = ttk.Button(pane,text= "click me too! ")
b2.pack(ipadx=10,ipady=10,side = TOP,fill="x")

b3 = ttk.Button(pane,text= "I'm also button!", command= master.destroy)
b3.pack(ipadx=10,ipady=10,side = TOP,fill="x")

b4 = ttk.Button(pane,text= "LEFT", command= master.destroy)
b4.pack(side = LEFT, expand=True, fill=BOTH)

b5 = ttk.Button(pane,text= "RIGHT", command= master.destroy)
b5.pack(side = RIGHT, expand=True, fill=BOTH)

b6 = ttk.Button(pane,text= "CENTER!", command= master.destroy)
b6.pack(side = LEFT, expand=True, fill=BOTH)


master.mainloop()