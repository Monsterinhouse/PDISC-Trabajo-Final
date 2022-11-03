# Imports
from cgitb import text
from distutils.command.upload import upload
from fileinput import filename
from struct import pack
from textwrap import fill
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from turtle import bgcolor, title
from PIL import Image, ImageTk
import tkinter as TTK

# Window Config
root = TTK.Tk()
root.title("Adaptador de Imagenes Web")

# TitleFrame
titleframe = Frame(root)
titleframe.config(bg="black", bd=3)
titleLabel = ttk.Label(titleframe, text="Adaptador de Imagenes Web", font=("Fixedsys", 20))
titleLabel.config(background='black', foreground='white')
titleLabel.grid(column=0, row=1, columnspan=6, padx=100)
titleframe.grid()

# UploadFrame
uploadframe = Frame(root)
uploadframe.config(bg="blue", bd=3)
uploadframe.grid(column=0, row=2, columnspan=3, rowspan=3, sticky=W)

# Procesos
def uploadImage () :
    global img
    f_types = [('JPG Files', '*.jpg'), ('PNG Files', '*.png'), ('All Files', '.*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    og_foto = Image.open(filename)
    res_file = og_foto.resize((300, 200))
    img = ImageTk.PhotoImage(res_file)
    img_button = ttk.Button(uploadframe,image=img) # using Button 
    img_button.grid(column=0, row=2, padx=20, pady=20)
    gen_button = ttk.Button(uploadframe, text="Generar Resultados", command=lambda:results(), width=45)
    gen_button.grid(column=0, row=4, padx=10, pady=10, columnspan=3)

def results() :
    # Result Frame
    resframe = Frame(root)
    resframe.config(bg="red", bd=3)
    resframe.grid(column=1, row=2, columnspan=3, rowspan=3, sticky=E)

# Componentes/Elementos
addButton = ttk.Button(uploadframe, text="Añadir Imagen", command=lambda:uploadImage(), width=45)

addButton.grid(column=0, row=3, padx=10, pady=20, columnspan=3)

root.mainloop()