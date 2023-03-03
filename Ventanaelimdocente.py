# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:44:39 2023

@author: win
"""

from tkinter import *
from tkinter.ttk import *
from Datos import Alumno

ventanaelim2=Tk()
ventanaelim2.resizable(False,False)
ventanaelim2.title("Eliminar docente")
ventanaelim2.geometry("500x300")
ventanaelim2.config(bg="#E2F9F9")


buscarld=Label(ventanaelim2,text="Nombre del docente a eliminar:")
buscarld.pack()
buscarld.place(x=150,y=60)

nota=Label(ventanaelim2,text="Si el docente no existe, no funcionará.")
nota.pack()
nota.place(x=10,y=270)

ebuscardoc=Entry(ventanaelim2,width=30)
ebuscardoc.pack()
ebuscardoc.place(x=150,y=110)


def elimdoc():
    textbuscar=ebuscardoc.get()
    with open("archivo2.txt", "r+") as archivox:
        lineas = archivox.readlines()
        for i, linea in enumerate(lineas):
            linea = linea.strip()
            if linea == textbuscar:
                del lineas[i:i+4]
                messagebox.showinfo("", "Docente eliminado con exito")
                ebuscardoc.delete(0,END)
                break
        archivox.seek(0)
        archivox.writelines(lineas)
        archivox.truncate()


botoneliminar4=Button(ventanaelim2,text="Eliminar",command=elimdoc)
botoneliminar4.pack()
botoneliminar4.place(x=200,y=170)

mainloop()