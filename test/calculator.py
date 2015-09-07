from Tkinter import *
import sys,os,core
import tkMessageBox
root = Tk(screenName = 'CalCulator',baseName='CalCulator')
root.title("CalCulator")
var = StringVar()
label = Label(root,anchor='n',textvariable = var, relief=RAISED,width=10,height=1,bg='black',justify='right',fg='white',font=('arial',30))
var.set("0")
label.pack()

frame = Frame(root)
frame.pack ()

frameTwo = Frame(root)
frameTwo.pack()

frameThree = Frame(root)
frameThree.pack()

frameFour = Frame(root)
frameFour.pack()

frameFive = Frame(root)
frameFive.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

def returnNum(x):
   buttonName = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"0",11:"*",12:"/",13:"+",14:"-",15:"="}
   if buttonName.has_key(x):
      return buttonName[x]
   else:
      tkMessageBox.showerror('Error','Value not found')
      
 
def setVal(x):
    val = returnNum(x)
    if val == "=":
        print 'result'
    else:
        print 'go on'
    
x = 1
heightOfButton = 2
widthOfButton  = 6
try:
    
    while x <= 15:
        if x <= 3:
             val = returnNum(x)
             button = Button(frame,text=x,width=widthOfButton,height=heightOfButton,command=(lambda text:lambda: setVal(text))(x))
             button.pack(side=LEFT)
             print  '1'
             
        elif x <= 6:
            buttonval = returnNum(x)
            button = Button(frameTwo,text=x,width=widthOfButton,height=heightOfButton,command=(lambda text:lambda: setVal(text))(x))
            button.pack(side=LEFT)
            print '2'
            
        elif x <= 9:
            button = Button(frameThree,text=x,width=widthOfButton,height=heightOfButton,command=(lambda text:lambda: setVal(text))(x))
            button.pack(side=LEFT)
            print '3'

        elif x <= 12:
            button = Button(frameFour,text=returnNum(x),width=widthOfButton,height=heightOfButton,command=(lambda text:lambda: setVal(text))(x))
            button.pack(side=LEFT)
            print '4'

        elif x <= 15:
            button = Button(frameFive,text=returnNum(x),width=widthOfButton,height=heightOfButton,command=(lambda text:lambda: setVal(text))(x))
            button.pack(side=LEFT)
         
        x += 1
     
        
except:
     tkMessageBox.showinfo("Error","Unknown Error Occured")
     root.destroy()
     sys.exit()
    
       
  

blackbutton = Button(bottomframe, text="Exit", fg="black",command=root.destroy,cursor='arrow')
blackbutton.pack( side = BOTTOM)

root.mainloop()
