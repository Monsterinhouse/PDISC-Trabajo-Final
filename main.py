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
root.title("Adaptador de Imagenes Web")
root.geometry("600x400")

# TitleFrame
titleframe = Frame(root)
titleframe.config(bg="black", bd=3)
titleLabel = ttk.Label(titleframe, text="Adaptador de Imagenes Web", font=("Fixedsys", 20))
titleLabel.config(background='black', foreground='white')
titleLabel.pack(fill=BOTH)
titleframe.pack(fill=BOTH)

# UploadFrame
uploadframe = Frame(root)
uploadframe.config(bg="blue", bd=3, width=300)
uploadframe.pack(fill=Y, expand=True)


# Procesos
def uploadImage () :
    global img
    f_types = [('JPG Files', '*.jpg'), ('PNG Files', '*.png'), ('All Files', '.*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    og_foto = Image.open(filename)
    res_file = og_foto.resize((300, 200))
    img = ImageTk.PhotoImage(res_file)
    img_button = ttk.Button(uploadframe,image=img) # using Button 
    img_button.pack(padx=40, pady=20)

# Componentes/Elementos
addbutton = ttk.Button(uploadframe, text="Añadir Imagen", command=lambda:uploadImage())

addbutton.pack(padx=30, pady=20, anchor=S, )

root.mainloop()