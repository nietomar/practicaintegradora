# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 00:25:49 2023

@author: win
"""
from tkinter import *
from tkinter.ttk import *

ventanaele=Tk()
ventanaele.resizable(False,False)
ventanaele.title("Eleccion")
ventanaele.geometry("500x300")
ventanaele.config(bg="#E2F9F9")

tl=Label(ventanaele,text="Elige una opción")
tl.place(x=210,y=50)


def botonal():
    ventanaele.destroy()
    from Ventanaalumno import Ventanaalumno
    
    
def botondocente():
    ventanaele.destroy()
    from Ventanadocente import Ventanadocente
    

botonal=Button(ventanaele,text="Alumno",command=botonal)
botonal.pack()
botonal.place(x=140,y=160)

botonmae=Button(ventanaele,text="Maestro",command=botondocente)
botonmae.pack()
botonmae.place(x=280,y=160)

mainloop()