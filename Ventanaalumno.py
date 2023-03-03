# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 00:38:36 2023

@author: win
"""

from tkinter import *
from tkinter.ttk import *
from Datos import Alumno

ventanaalumno=Tk()
ventanaalumno.resizable(False,False)
ventanaalumno.title("Alumno")
ventanaalumno.geometry("500x300")
ventanaalumno.config(bg="#E2F9F9")

ln=Label(ventanaalumno,text="Nombre:")
ln.pack
ln.place(x=150,y=30)

nom=StringVar()
bol=StringVar()
grup=StringVar()

enom=Entry(ventanaalumno,width=30,textvariable=nom)
enom.pack()
enom.place(x=150,y=50)

lb=Label(ventanaalumno,text="Boleta:")
lb.pack
lb.place(x=150,y=90)

ebol=Entry(ventanaalumno,width=30,textvariable=bol)
ebol.pack()
ebol.place(x=150,y=110)


lg=Label(ventanaalumno,text="Grupo:")
lg.pack
lg.place(x=150,y=150)

egrou=Entry(ventanaalumno,width=30,textvariable=grup)
egrou.pack()
egrou.place(x=150,y=170)


def guardar():
    nombre=nom.get()
    boleta=bol.get()
    grupo=grup.get()
    
    if any(char.isdigit() for char in nombre) or len(nombre)<2:
            messagebox.showerror("Error","El nombre tiene 2 o mas letras y no contiene numeros")
    else:
        if boleta.isdigit()!=True:
            messagebox.showerror("Error","La boleta debe tener 10 digitos")
        else:
            if len(boleta)!=10:
                messagebox.showerror("Error","La boleta debe tener 10 digitos")
            else:
                if len(grupo)<4 or len(grupo)>5:
                    messagebox.showerror("Error","El grupo debe tener de 4 a 5 digitos")
                else:
                    
                    messagebox.showinfo("","Datos guardados")
                    from Datos import Alumno
                    
                    Alumno=Alumno(nombre,boleta,grupo)
                    Alumno.guardar()
                    
                    enom.delete(0,END)
                    ebol.delete(0,END)
                    egrou.delete(0,END)


def consultar():
    archivo=open("archivo.txt","r")
    registros=archivo.read()
    archivo.close()
    messagebox.showinfo("Alumnos: ", registros)
    

def funbotoneliminaralu():
    ventanaalumno.destroy()
    from Ventanaelimalumno import Ventanaelimalumno


botonreg1=Button(ventanaalumno,text="Registrar",command=guardar)
botonreg1.pack()
botonreg1.place(x=50,y=240)


botonconsul1=Button(ventanaalumno,text="Consultar",command=consultar)
botonconsul1.pack()
botonconsul1.place(x=210,y=240)


botoneliminar1=Button(ventanaalumno,text="Eliminar",command=funbotoneliminaralu)
botoneliminar1.pack()
botoneliminar1.place(x=380,y=240)


mainloop()