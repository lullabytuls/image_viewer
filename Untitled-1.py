from tkinter import *

from PIL import ImageTk, Image

root=Tk()

root.title("Image Viewer")
root.configure(bg="light blue")
im1=PhotoImage(file='D:/git-codes/image_viewer/images/un.png')
im2=PhotoImage(file='D:/git-codes/image_viewer/images/dos.png')
im3=PhotoImage(file='D:/git-codes/image_viewer/images/tres.png')

images= [im1,im2,im3]
label= Label(image=im1)

def forward(num):
    global label
    global button_back 
    global button_forward 

    label.grid_forget()
    label= Label(image=images[num-1])
    button_forward =Button(root, text=">>", bg='white', activebackground='yellow', command = lambda: forward(num+1))
    button_back= Button(root, text="<<",bg='white', activebackground='yellow', command= lambda: backward(num-1))
    
    if num==3:
        button_forward= Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=2)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1 , column=1)

    
def backward(num):
    global label
    global button_back 
    global button_forward 

    label.grid_forget()
    label= Label(image=images[num-1])
    button_forward =Button(root, text=">>", bg='white', activebackground='yellow', command = lambda: forward(num+1))
    button_back= Button(root, text="<<", bg='white', activebackground='yellow', command= lambda: backward(num-1))
    
    if num==1:
        button_back= Button(root, text="<<", state=DISABLED)
        
    label.grid(row=0, column=0, columnspan=2)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1 , column=1)



button_back= Button(root, text="<<",bg='white', activebackground='yellow',command=backward, state=DISABLED)
button_forward = Button(root, text=">>",bg='white', activebackground='yellow', command = lambda: forward(2))


label.grid(row=0, column=0, columnspan=2)
button_back.grid(row=1, column=0)
button_forward.grid(row=1 , column=1)


root.mainloop()