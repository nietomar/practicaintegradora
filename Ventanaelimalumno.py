# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:50:54 2023

@author: win
"""
from tkinter import *
from tkinter.ttk import *
from Datos import Alumno

ventanaelim=Tk()
ventanaelim.resizable(False,False)
ventanaelim.title("Eliminar alumno")
ventanaelim.geometry("500x300")
ventanaelim.config(bg="#E2F9F9")


buscarl=Label(ventanaelim,text="Nombre del alumno a eliminar:")
buscarl.pack()
buscarl.place(x=150,y=60)


nota=Label(ventanaelim,text="Si el alumno no existe, no funcionará.")
nota.pack()
nota.place(x=10,y=270)


ebuscar=Entry(ventanaelim,width=30)
ebuscar.pack()
ebuscar.place(x=150,y=110)


def elim():
    textbuscar=ebuscar.get()
    with open("archivo.txt", "r+") as archivof:
        lineas = archivof.readlines()
        for i, linea in enumerate(lineas):
            linea = linea.strip()
            if linea == textbuscar:
                del lineas[i:i+4]
                messagebox.showinfo("", "Alumno eliminado con exito")
                ebuscar.delete(0,END)
                break
        archivof.seek(0)
        archivof.writelines(lineas)
        archivof.truncate()


botoneliminar3=Button(ventanaelim,text="Eliminar",command=elim)
botoneliminar3.pack()
botoneliminar3.place(x=200,y=170)

mainloop()