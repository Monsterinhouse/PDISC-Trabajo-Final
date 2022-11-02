# Imports
from cgitb import text
from distutils.command.upload import upload
from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from turtle import bgcolor, title
from PIL import Image, ImageTk
import tkinter as TTK

# Window Config
root = TTK.Tk()
root.title("Adaptador de Imagenes")
root.geometry("600x400")

# TitleFrame
titleframe = Frame(root)
titleframe.config(bg="black", bd=3)
titleLabel = ttk.Label(titleframe, text="Adaptador de Imagenes Web", font=("Fixedsys", 20))
titleLabel.config(background='black', foreground='white')
titleLabel.pack(fill=BOTH)
titleframe.pack(fill=BOTH)

# UploadFrame
uploadframe = Frame(root, width=300, height=200)
uploadframe.config(bg="blue", bd=3)
uploadLabel = ttk.Label(uploadframe, text="Something", font=("Fixedsys", 12))
uploadLabel.config(background='blue', foreground='white')
uploadLabel.pack(anchor=W)
uploadframe.pack(fill=Y)


# Procesos
def uploadImage () :
    global img
    f_types = [('JPG Files', '*.jpg'), ('PNG Files', '*.png'), ('All Files', '.*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    og_foto = Image.open(filename)
    res_file = og_foto.resize((300, 200))
    img = ImageTk.PhotoImage(res_file)
    img_button = ttk.Button(root,image=img) # using Button 
    img_button.pack()

# Componentes/Elementos
addbutton = ttk.Button(root, text="Añadir Imagen", command=lambda:uploadImage())

addbutton.pack()

root.mainloop()