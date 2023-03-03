# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:52:35 2023

@author: win
"""

from tkinter import *
from tkinter.ttk import *


window =Tk()
window.resizable(False,False)
window.title("Ingresar")
window.geometry("500x300")

window.config(bg="#E2F9F9")

logusuario=Label(window,text="Ingresar Usuario")
logusuario.pack()
logusuario.place(x=150,y=60)


usuario=StringVar()
contrasena=StringVar()


eusu=Entry(window,width=30,textvariable=usuario)
eusu.pack()
eusu.place(x=150,y=80)


logcontra=Label(window,text="Contraseña")
logcontra.pack()
logcontra.place(x=150,y=130)



econtra=Entry(window,width=30,show="*",textvariable=contrasena)
econtra.pack()
econtra.place(x=150,y=150)


sus=Label(window,text="Usuario: tppc")
sus.pack()
sus.place(x=360,y=100)

sus=Label(window,text="Contraseña: progra09")
sus.pack()
sus.place(x=360,y=130)


def login():
    usuario1 = usuario.get()
    contrasena1 = contrasena.get()
    if usuario1 == "tppc" and contrasena1 == "progra09":
        window.destroy()
        from Ventanaeleccion import Ventanaeleccion
    else:
        messagebox.showwarning("Error","Usuario o contraseña incorrectos")



botonentrar=Button(window,text="Entrar",cursor="hand2",command=login)
botonentrar.pack()
botonentrar.place(x=200,y=200)


mainloop()