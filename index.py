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