from Tkinter import *
import tkMessageBox,sys,os
import codes,tkFileDialog
root = Tk()

frameOne  = Frame(root)
frameOne.pack()

root.title("File Deleter")
button = Button(frameOne,text='Choose File',width=10,height=2,command=codes.retLink)
button.pack(side=LEFT)

root.mainloop()
