from tkinter import ttk
from tkinter import *

class Operaciones:

    def __init__(self, window):
        ancho = 700
        alto = 400

        self.wind = window
        self.wind.geometry(str(ancho)+'x'+str(alto))
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Exámen Final')

        frame = LabelFrame(self.wind, text = 'Exámen final')
        frame.grid(row = 0, column = 0, columnspan = 10, pady = 50)

        Label(frame, text = '¡BIENVENIDO!',font=("Arial",33)).grid(row = 0,columnspan= 6)

        Label(frame, text = 'Nombre: ').grid(row = 1,columnspan = 3)
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1,columnspan = 6)
        Label(frame, text = 'Apellido: ').grid(row = 2,columnspan = 3)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2,columnspan = 6)
        Label(frame, text = 'Día: ').grid(row = 3,columnspan = 3)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, columnspan = 6)
        Label(frame, text = 'Mes: ').grid(row = 4,columnspan = 3)
        self.var4 = Entry(frame)
        self.var4.grid(row = 4, columnspan = 6)
        Label(frame, text = 'Año: ').grid(row= 5,columnspan = 3)
        self.var5 = Entry(frame)
        self.var5.grid(row = 5, columnspan = 6)
        
        ttk.Button(frame, text = 'Funcion 1', command = self.botton1).grid(row = 6, column = 1, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 2', command = self.botton2).grid(row = 6, column = 2, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 3', command = self.botton3).grid(row = 6, column = 3, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 4', command = self.botton4).grid(row = 6, column = 4, sticky = W + E)
        ttk.Button(frame, text = 'Funcion 5', command = self.botton5).grid(row = 6, column = 5, sticky = W + E)

