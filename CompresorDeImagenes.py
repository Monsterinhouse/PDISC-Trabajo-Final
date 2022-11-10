# Imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import *
import PIL
from PIL import Image, ImageTk
import tkinter as TTK


# Window Config
root = TTK.Tk()
root.title("Adaptador de Imagenes Web")
root.config(bg='black')


# TitleFrame
titleframe = Frame(root)
titleframe.config(bg="black", bd=3)
titleLabel1 = ttk.Label(titleframe, text="Adaptador de", font=("Fixedsys", 18))
titleLabel1.config(background='black', foreground='white')
titleLabel1.grid(column=0, row=1)
titleLabel2 = ttk.Label(titleframe, text="Imagenes Web", font=("Fixedsys", 18))
titleLabel2.config(background='black', foreground='white')
titleLabel2.grid(column=0, row=2)
titlelabel3 = ttk.Label(titleframe, text="Hecho Por", font=("Fixedsys", 18))
titleframe.grid()

# UploadFrame
uploadframe = Frame(root)
uploadframe.config(bg="blue", bd=3)
uploadframe.grid(column=0, row=3, rowspan=2)

# Procesos
def uploadImage () :
    global img
    global og_foto
    global res_file
    global myHeight
    global myWidth
    f_types = [('JPG Files', '*.jpg'), ('PNG Files', '*.png'), ('All Files', '.*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    og_foto = PIL.Image.open(filename)
    res_file = og_foto.resize((300,200))
    img = ImageTk.PhotoImage(res_file)
    img_button = ttk.Button(uploadframe,image=img) # using Button 
    img_button.grid(column=0, row=4, padx=20, pady=20)
    gen_button = ttk.Button(uploadframe, text="Generar Resultados", command=lambda:results(), width=45)
    gen_button.grid(column=0, row=6, padx=10, pady=10, columnspan=3)
    myHeight, myWidth = og_foto.size

def save() :
    save_path = asksaveasfilename()
    compressed_img = og_foto.resize((myHeight,myWidth), PIL.Image.ANTIALIAS)
    compressed_img.save(save_path + "_comprimido.jpg")

def results() :
    # Result Frame
    resframe = Frame(root)
    resframe.config(bg="red", bd=3, width=200)
    res_label = Label (resframe, text="Resultado", font=('Impact', 15))
    res_img = ttk.Button(resframe, image=img)
    res_save = ttk.Button(resframe, text="Guardar Resultado", command=lambda:save())
    res_label.config(bg="red", fg='white')
    res_label.grid (column=1, row=5)
    res_img.grid(column=1, row=4, padx=20, pady=20)
    res_save.grid(column=1, row=6, pady=27)
    resframe.grid(column=1, row=1, columnspan=3, rowspan=3)

# Componentes/Elementos
addButton = ttk.Button(uploadframe, text="Añadir Imagen", command=lambda:uploadImage(), width=45)

addButton.grid(column=0, row=5, padx=10, pady=20, columnspan=3)

root.mainloop()