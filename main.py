

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile
import os

root = Tk ()
root.geometry ("500x580")
root.wm_iconbitmap("1.ico")
root.title("Untitled - Notepad")

def openFile():
    global data
    data=askopenfilename(defaultextension=".txt",
                         filetypes=[("Text Documents","*.txt"),
                                    ("Text Documents","*.txt")])
    if data=="":
        data=None
        pass
    else:
        root.title(os.path.basename(data)+" - Notepad")
        textarea.delete(1.0,END)
        file=open(data,"r")
        textarea.insert(1.0,file.read())
    pass
def saveFile():
    global data

    if data ==None:
        data=asksaveasfile(initialfile="Untitled.txt",
                           defaultextension=".txt",
                           filetypes=[("Text Documents","*.txt"),
                                      ("Text Documents","*.txt")])
        if data == "":
            data = None
            pass
        else:

            temp=data.name
            file = open(f"{temp}", "w")
            file.write(textarea.get(1.0,END))
            file.close()
            root.title(f"{os.path.basename(temp)}")
        pass
    else:

        file = open(data, "w")
        file.write(textarea.get(1.0,END))
        file.close()
        pass

def newFile():
    global data
    data=None
    root.title("Untitled - Notepad")
    textarea.delete(1.0,END)
    pass
def cut():
    textarea.event_generate(("<<Cut>>"))
    pass
def copy():
    textarea.event_generate(("<<Copy>>"))
    pass
def paste():
    textarea.event_generate(("<<Paste>>"))
    pass
def help():
    showinfo("Thanks for viewing","Follow us for for exciting projects")
    pass


menubar = Menu (root)

data=None  #variabe for storing file
# file menu

file = Menu(menubar,tearoff=0)
file.add_command (label = "New...", command = newFile)
file.add_command (label = "Open", command = openFile)
file.add_command (label = "Save", command = saveFile)
file.add_separator()
file.add_command (label = "Exit", command = exit)
menubar.add_cascade (label = "File", menu = file)

# Edit menu

edit = Menu(menubar,tearoff=0)
edit.add_command (label = "Cut", command = cut)
edit.add_command (label = "Copy", command = copy)
edit.add_command (label = "Paste", command = paste)
menubar.add_cascade (label = "Edit", menu = edit)

#Help menu

helpM=Menu(menubar,tearoff=0)
helpM.add_command (label = "About Notepad", command = help)
menubar.add_cascade (label = "Help", menu = helpM)

root.config (menu = menubar)


# text area

textarea=Text(root,font="calibri 16 normal")
barY=Scrollbar(root)                           #adding scrollBar
barY.pack(side=RIGHT,fill=Y)                   #compulsory
barY.config(command=textarea.yview)            #compulsory
textarea.config(yscrollcommand=barY.set)       #compulsory
textarea.pack(fill=BOTH,expand=1)

root.mainloop ()

