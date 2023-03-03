# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 01:27:10 2023

@author: win
"""

from tkinter import *
from tkinter.ttk import *
from Datos import Docente
from io import *

ventanadocente=Tk()
ventanadocente.resizable(False,False)
ventanadocente.title("Docente")
ventanadocente.geometry("500x300")
ventanadocente.config(bg="#E2F9F9")

lnomd=Label(ventanadocente,text="Nombre:")
lnomd.pack
lnomd.place(x=150,y=30)

nomd=StringVar()
rfcd=StringVar()
correod=StringVar()

enom=Entry(ventanadocente,width=30,textvariable=nomd)
enom.pack()
enom.place(x=150,y=50)

lb=Label(ventanadocente,text="RFC:")
lb.pack
lb.place(x=150,y=90)

erfc=Entry(ventanadocente,width=30,textvariable=rfcd)
erfc.pack()
erfc.place(x=150,y=110)


lgd=Label(ventanadocente,text="Correo:")
lgd.pack
lgd.place(x=150,y=150)

ecorr=Entry(ventanadocente,width=30,textvariable=correod)
ecorr.pack()
ecorr.place(x=150,y=170)


def botonreg():

    nombre=nomd.get()
    rfc=rfcd.get()
    correo=correod.get()
    
    if any(char.isdigit() for char in nombre) or len(nombre)<2:
            messagebox.showerror("Error","El nombre tiene 2 o mas letras y no contiene números")
    else:
        if len(rfc)!=13:
            messagebox.showerror("Error","El RFC debe tener 13 caracteres")
        else:
            if len(correo)<3:
                messagebox.showerror("Error","El correo debe tener más de 2 caracteres")
            else:
                messagebox.showinfo("","Datos guardados")
                from Datos import Docente
                
                Docente=Docente(nombre,rfc,correo)
                Docente.guardar()
                
                enom.delete(0,END)
                erfc.delete(0,END)
                ecorr.delete(0,END)


def consultar():
    archivo=open("archivo2.txt","r")
    registros=archivo.read()
    archivo.close()
    messagebox.showinfo("Docentes: ", registros)
    
def funbotoneliminardoc():
    ventanadocente.destroy()
    from Ventanaelimdocente import Ventanaelimdocente
    

botonreg2=Button(ventanadocente,text="Registrar",command=botonreg)
botonreg2.pack()
botonreg2.place(x=50,y=240)


botonconsul2=Button(ventanadocente,text="Consultar",command=consultar)
botonconsul2.pack()
botonconsul2.place(x=210,y=240)


botoneliminar2=Button(ventanadocente,text="Eliminar",command=funbotoneliminardoc)
botoneliminar2.pack()
botoneliminar2.place(x=380,y=240)

mainloop()