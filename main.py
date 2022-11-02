from distutils.command.upload import upload
from fileinput import filename
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as TTK

root = TTK.Tk()

root.title("Adaptador de Imagenes")
root.geometry("600x400")

def uploadImage () :
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =TTK.Button(root,image=img) # using Button 
    b2.grid(row=3,column=1)
    scrollbar = TTK.Scrollbar(root, orient="vertical", command=img.yview)
    scrollbar.grid(row=0, column=1, sticky=TTK.NS)


titleLabel = TTK.Label(root, text="Adaptador de Imagenes Web", font=("Helvetica", 20))
addbutton = TTK.Button(root, text="Añadir Imagen", command=lambda:uploadImage())

titleLabel.grid(column=1, row=0, padx=2, pady=2)
addbutton.grid(column=1, row=4)

root.mainloop()