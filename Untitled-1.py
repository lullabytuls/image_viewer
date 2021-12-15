from tkinter import *

from PIL import ImageTk, Image

root=Tk()

root.title("Image Viewer")

im1=ImageTk.PhotoImage(Image.open('un.png'))
im2=ImageTk.PhotoImage(Image.open('dos.png'))
im3=ImageTk.PhotoImage(Image.open('tres.png'))

images= [im1,im2,im3]



label= Label(image=im1)
root.mainloop()