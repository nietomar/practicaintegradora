# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 01:53:27 2023

@author: win
"""

from tkinter import *
nombre=str()
class Alumno:
    
    def __init__(self,nombre,boleta,grupo):
        self.nombre = nombre
        self.boleta = boleta
        self.grupo = grupo
        
    def getNombre(self):
        return self.nombre
    
    def getBoleta(self):
        return self.boleta
    
    def getGrupo(self):
        return self.grupo
    
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setBoleta(self,boleta):
        self.__boleta = boleta
        
    def setgrupo(self,grupo):
        self.__grupo = grupo
        
    def guardar(self): 
            
        archivo=open("archivo.txt","a")
        archivo.write(self.nombre)
        archivo.write("\n")
        archivo.write(self.boleta)
        archivo.write("\n")
        archivo.write(self.grupo)
        archivo.write("\n")
        archivo.write("-----------------")
        archivo.write("\n")
        archivo.close()
        
class Docente:
    
    def __init__(self,nombre,rfc,correo):
        self.nombre = nombre
        self.rfc = rfc
        self.correo = correo
        
    def getNombre(self):
        return self.nombre
    
    def getRfc(self):
        return self.rfc
    
    def getCorreo(self):
        return self.correo
    
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setRfc(self,boleta):
        self.__rfc = rfc
        
    def setCorreo(self,grupo):
        self.__correo = correo
        
        
    def guardar(self): 
        
        archivo=open("archivo2.txt","a")
        archivo.write(self.nombre)
        archivo.write("\n")
        archivo.write(self.rfc)
        archivo.write("\n")
        archivo.write(self.correo)
        archivo.write("\n")
        archivo.write("-----------")
        archivo.write("\n")
        archivo.close()
        