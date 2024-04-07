from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title("MaxTechnology")
root.geometry("%dx%d+%d+%d"%(800,550,10,30))
root.configure(bg="#00003f")
root.resizable(False,False)
user=[]

frame=Frame(root,width=235,height=290,border=0)
frame.configure(bg="#00003f")
frame.place(x=15,y=30)