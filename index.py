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

        self.resultado = Label(self.wind, text = '', fg = 'red')
        self.resultado.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    def validacion1(self):
        return len(self.var1.get()) != " " and len(self.var2.get()) != 0 and len(self.var3.get()) != " "

    def validacion2(self):
       return len(self.var3.get()) != 0 and len(self.var3.get()) != 0 and len(self.var3.get()) != 0 and len(self.var5.get()) != 0 and len(self.var3.get()) != 0

    def botton1(self):
        if self.validacion2():
            dia=int(self.var3.get())
            mes=int(self.var4.get())
            año=int(self.var5.get())
            hdia= format(dia, "0x" )
            hmes= format(mes, "0x" ) 
            haño= format(año, "0x" )
            self.resultado['text'] = 'Fecha: {}/{}/{} Fecha en binario:{}/{}/{}'.format(dia,mes,año,hdia,hmes,haño)
        else:
            self.resultado['text'] = 'Poner datos en las casillas'

    def botton2(self):
        if self.validacion2():
            dia=int(self.var3.get())
            mes=int(self.var4.get())
            año=int(self.var5.get())
            aaños= 2019 - año
            aañoss=24*(31*(aaños*12))
            mmeses=24*(31*mes)
            ddias=dia*24
            resultado= aañoss + mmeses + ddias
            self.resultado['text'] = 'Usted nació en {}/{}/{} y ha vivido {} horas'.format(dia,mes,año,resultado)
        else:
            self.resultado['text'] = 'Poner datos en las casillas'

    def botton3(self): 
        if self.validacion1():
            nombre=str(self.var1.get())
            apellido=str(self.var2.get())
            numero_nombre=int(len(nombre))
            numero_apellido=int(len(apellido))
            sumatoria= numero_nombre + numero_apellido
            if sumatoria %2==0 :
               self.resultado['text'] = '{} {}, Su nombre junto con su apellido es par'.format(nombre,apellido)
            else:
                self.resultado['text'] = '{} {}, Su nombre junto con su apellido es impar'.format(nombre,apellido)
        else:
            self.resultado['text'] = 'Poner datos en las casillas'

    def botton4(self):
        if self.validacion1():
            nombre=str(self.var1.get())
            apellido=str(self.var2.get())
            cuenta1 = 0
            cuenta2 = 0
            for num in nombre:
                if num == 'a' or num =='A' or num =='e' or num =='E' or num =='i' or num=='I' or num=='o' or num=="O" or num=="u" or num=="U":
                    cuenta1 += 1
            for num in apellido:
               if num == 'a' or num =='A' or num =='e' or num =='E' or num =='i' or num=='I' or num=='o' or num=="O" or num=="u" or num=="U":
                  cuenta2 += 1
            nom1=len(nombre)
            apell2=len(apellido)
            vocal1 = cuenta1
            vocal2 = cuenta2
            consonante1 = nom1-cuenta1 
            consonante2 = apell2-cuenta2
            self.resultado['text'] = '{} tiene {} vocales y {} consonantes Y {} tiene {} vocales y {} consonantes'.format(nombre,vocal1,consonante1,apellido,vocal2,consonante2)
        else:
            self.resultado['text'] = 'Poner datos en las casillas'

    def botton5(self):
        if self.validacion1():
            nombre=str(self.var1.get())
            apellido=str(self.var2.get())
            nombre_invertido = ""
            apellido_invertido1= ""
            for letra in nombre:
                nombre_invertido = letra + nombre_invertido
            for letra1 in apellido:
                apellido_invertido1 = letra1 + apellido_invertido1
            self.resultado['text'] = '{} {} Al revés es: {} {}'.format(nombre,apellido,nombre_invertido,apellido_invertido1)
        else:
            self.resultado['text'] = 'Poner datos en las casillas'
