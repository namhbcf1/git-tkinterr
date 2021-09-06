from os import name
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd 

root = tk.Tk()
# root.geometry("750x500")
root.resizable(False,False)
def callback(): 
    name= fd.askdirectory() 
    print(name)
    return name

box = ttk.Button(root,text = "name")
box.grid(row=1,column=1,sticky=W,padx=20)
box = ttk.Button(root,text = "size")
box.grid(row=1,column=1,sticky=W,padx=108)
box = ttk.Button(root,text = "DATE MODIFY")
box.grid(row=1,column=1,sticky=E,padx=108)
box = ttk.Button(root,text = "EXTENTION")
box.grid(row=1,column=1,sticky=E,padx=20)

myscroll = Scrollbar(root) 
PATH_1 = ttk.Label(root, text=callback())
PATH_1.grid(row = 0, column = 1,padx=20, ipadx=100)

mylist2 = Listbox(root, yscrollcommand = myscroll.set )  
for line in range(1, 100): 
    mylist2.insert(END, "Number " + str(line)) 
mylist2.grid(padx=20,row = 2, column = 1, ipadx=100,ipady=40) 

mylabel1 = Label(root, text ='PATH', font = "30")  
mylabel1.grid(row = 0, column = 0, sticky = NE) 

mylabel2 = Label(root, text ='DICTIONARY', font = "30")  
mylabel2.grid(row = 1, column = 0, sticky = W, pady = 2) 
 
checkbox1= ttk.Checkbutton(root,text = "return")
checkbox1.grid(row = 2, column = 2,padx=20,pady=20,sticky=NW)

checkbox2= ttk.Checkbutton(root,text = "arrange")
checkbox2.grid(row = 2, column = 2,padx=20,pady=20,sticky=W)

control_variable = tk.StringVar(root)
OPTION_TUPLE = ("Arrange by name", "Arrange by size", "Arrange by DATEMODIFY","Arrange by EXTENTION") 
optionmenu_widget = ttk.OptionMenu(root,
                     control_variable, *OPTION_TUPLE)
optionmenu_widget.grid(row = 2, column = 2,padx=20,pady=20,sticky=SW)

mylist = Listbox(root, yscrollcommand = myscroll.set )  
for line in range(1, 100): 
    mylist.insert(END, "Number " + str(line)) 
mylist.grid(row = 2, column = 0, sticky = W,ipadx=0, ipady = 40)  
myscroll.config(command = mylist.yview)  


    
but_1 = tk.Button(root, text="CANCEL ", bg="red", fg="white",command=root.destroy)
but_1.grid(row = 3, column = 2, sticky = S, pady = 2, ipadx=15)
but_2 = tk.Button(root, text="OK ", bg="red", fg="white",command=root.destroy)
but_2.grid(row = 3, column = 2, sticky = S, pady = 40, ipadx=30)


    
errmsg = 'Error!'
tk.Button(text='Click to Open Folder', 
       command=callback).grid(row = 0, column = 2,padx=20, ipadx=100)

root.mainloop()