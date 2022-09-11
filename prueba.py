# Python program to create a table
import tkinter
from tkinter import *

root = tkinter.Tk()

canvas1 = tkinter.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tkinter.Entry(root)
canvas1.create_window(200, 140, window=entry1)

lista = []


def getSquareRoot():
    x1 = entry1.get()

    # for i in range(21):
    #     lista.append(i)
    lista.append(x1)  #BUG, HAY QUE METER 20 (0-20) DATOS Y DESPUES CERRARLO

    label1 = tkinter.Label(root, text="Valor Agregado: "+x1)
    canvas1.create_window(200, 230, window=label1)


button1 = tkinter.Button(text='Agregar', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

print("Frecuencia de los datos:")
print(lista)


class Table:

    def __init__(self, root):


        #FRECUENCIA ACUMULADA
        fi = []
        fi.append(lista[0])
        for i in range(20):
            fi.append(int(fi[i])+int(lista[i+1]))
        print("Frecuencia Acumulada de los datos: ")
        print(fi)

        lst = [("X", "fi", 'Fi', "hi", "Hi", "%", "% acumulado"),
               (1, lista[0], fi[0], 19, 1, 'Raj', 'Mumbai'),
               (2, lista[1], fi[1], 18, 1, 'Raj', 'Mumbai'),
               (3, lista[2], fi[2], 20, 1, 'Raj', 'Mumbai'),
               (4, lista[3], fi[3], 21, 1, 'Raj', 'Mumbai'),
               (5, lista[4], fi[4], 21, 1, 'Raj', 'Mumbai'),
               (6, lista[5], fi[5], 19, 1, 'Raj', 'Mumbai'),
               (7, lista[6], fi[6], 18, 1, 'Raj', 'Mumbai'),
               (8, lista[7], fi[7], 20, 1, 'Raj', 'Mumbai'),
               (9, lista[8], fi[8], 21, 1, 'Raj', 'Mumbai'),
               (10, lista[9], fi[9], 21, 1, 'Raj', 'Mumbai'),
               (11, lista[10], fi[10], 19, 1, 'Raj', 'Mumbai'),
               (12, lista[11], fi[11], 18, 1, 'Raj', 'Mumbai'),
               (13, lista[12], fi[12], 20, 1, 'Raj', 'Mumbai'),
               (14, lista[13], fi[13], 21, 1, 'Raj', 'Mumbai'),
               (15, lista[14], fi[14], 21, 1, 'Raj', 'Mumbai'),
               (16, lista[15], fi[15], 19, 1, 'Raj', 'Mumbai'),
               (17, lista[16], fi[16], 18, 1, 'Raj', 'Mumbai'),
               (18, lista[17], fi[17], 20, 1, 'Raj', 'Mumbai'),
               (19, lista[18], fi[18], 21, 1, 'Raj', 'Mumbai'),
               (20, lista[19], fi[19], 21, 1, 'Raj', 'Mumbai')]

        total_rows = len(lst)
        total_columns = len(lst[0])

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 11, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data


# create root window
root = Tk()
t = Table(root)
root.mainloop()
