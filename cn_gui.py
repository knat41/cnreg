'''
Jan 2023
@author: CN Team
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

# Used to clean and analyse the data-set
import pandas as pd

from cn_var import *

datalist = ['m3.xls']
dflist = []
all_student  = pd.read_pickle("dummy.pkl", compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1})
dfs = getData2Frame(all_student)
# Create instance
win = tk.Tk()   

# Add a title       
win.title("CN Data Science for Student")  
win.rowconfigure(0, minsize=640, weight=1)
win.columnconfigure(1, minsize=800, weight=1)

# We are creating a container frame to hold all other widgets
mighty = ttk.LabelFrame(win, text=' Please enter you student ID')
mighty.grid(column=1, row=0, padx=8, pady=4)

# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(mighty, text="Enter a ID:")
a_label.grid(column=0, row=0, sticky='W')

def loadData():    
    all_student = getData2Frame(all_student)
    _msgTextBox(all_student.shape)

# Define a function to close the window
def exitwindow():
    win.destroy()

# Modified Button Click Function
def click_me():
    gpax, gpagroup = getGPAX(dfs, name.get())
    _msgTextBox(formatGPA(gpax))
    action.configure(text=name.get() + ' GPAX ' + formatGPA(gpax) +' ')
    plotGPA(gpagroup)

# Display a Message Box
def _msgBox():
    msg.showinfo('Info Box', 'Data Science Tool:\ncn team 2023.')  

# Display a Message Box
def _msgDoneBox():
    msg.showinfo('Info Box', 'Done')

# Display a Message Box
def _msgTextBox(info):
    msg.showinfo('Info Box', info)
    
# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# Adding a Button
action = ttk.Button(mighty, text="Select!", command=click_me)   
action.grid(column=2, row=1)                                

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar)
#file_menu.add_command(label="Prepare Data", command=getData2Frame)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exitwindow)
menu_bar.add_cascade(label="File", menu=file_menu)


# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
menu_bar.add_cascade(label="Help", menu=help_menu)

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()