import tkMessageBox,tkFileDialog,sys,os

def retLink():
     filename = tkFileDialog.askopenfilename()
     if filename:
         delFile(filename)
     else:
        #tkMessageBox.showerror("Error","Please select some files")

    
def delFile(x):
    if x:
       try:
           os.remove(x)
           tkMessageBox.showinfo("Success","The File has been deleted SuccessFully")
       except:
            tkMessageBox.showerror("Error","File Has been Deleted or not available")
            sys.exit()
    else:
        tkMessageBox.showerror("Error","Empty FileName")
        sys.exit()
