from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
from sympy import *
import numpy as np
import segment
import preprocess


def process(path):
    global ans1
    ans1=segment.segment(path)
    label=Label(text="Predicted Output(Edit if there is any error)",font="Helvetica 12 bold")
    label.place(x=10,y=540)
    txt1 = Entry(root, textvariable=result,width=70,font = "Helvetica 20 bold").place(x=10,y=570)
    result.set(ans1)
    label1=Label(text="Solution",font="Helvetica 12 bold")
    label1.place(x=10,y=610)
    txt2=Entry(root,textvariable=solved,state="disabled",width=70,font="Helvetica 20 bold").place(x=10,y=640)
    
    

def integral():
    #print(integrate(result.get(),symbols('x')))
    
    eq=preprocess.preprocess(result.get())
    solved.set(integrate(eq))
    
def dif():
    
    eq=preprocess.preprocess(result.get())
    a=diff(eq)
    solved.set(a)
    
def quad():

    eq=preprocess.preprocess(result.get())
    solved.set(solve(eq,dict=True))
    
def calc():
    
    eq=preprocess.preprocess(result.get())
    #r=eq.split(" ")
    solved.set(eval(eq))
    
    
    
def select_image():
    # grab a reference to the image panels
    global panelA
    global path

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image=cv2.resize(image,(1200,500))

        # convert the images to PIL format...
        image = Image.fromarray(image)
        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
            # update the pannels
        panelA.configure(image=image)
        panelA.image = image
        panelA.place(x=10,y=40)
        #process(path)
        
            

# initialize the window toolkit along with the two image panels
root=Tk()
root.geometry("1400x700")

panelA=None
path=""
result=StringVar()
solved=StringVar()
ans1=""

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI

heading=Label(text="Mathematical Equation Computing",font="Helvetica 20 bold")
heading.place(x=430,y=5)

panel=PanedWindow(root,borderwidth=15,orient = VERTICAL,sashpad="20",background="black")
panel.place(x=1240,y=50)


            
btn1 = Button(panel, text="Select an image", command=select_image)
panel.add(btn1)

#btn1.place(x=1270,y=100)
btn2 = Button(panel,text="Process",command= lambda : process(path))
panel.add(btn2)
#btn2.place(x=1270,y=10)

panelA = Label(text="Insert an Image",font="Helvetica 40 bold")
panelA.place(x=400,y=200)


btn3=Button(panel,text="Integrate",command=lambda : integral())
panel.add(btn3)


btn4=Button(panel,text="Differentiate",command=lambda : dif())
panel.add(btn4)

btn5=Button(panel,text="Equation Solution",command=lambda : quad())
panel.add(btn5)

btn6=Button(panel,text="Simple Calculation",command=lambda : calc())
panel.add(btn6)

# kick off the GUI
root.mainloop()
