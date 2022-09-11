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

    lista.append(x1)

    label1 = tkinter.Label(root, text=x1)
    canvas1.create_window(200, 230, window=label1)


button1 = tkinter.Button(text='Agregar', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

print(lista)


class Table:

    def __init__(self, root):
        x = int(lista[0])


        lst = [("X", "fi", 'Fi', "hi", "Hi", "%", "% acumulado"),
               (1,  lista[0] , x, 19, 1, 'Raj', 'Mumbai'),
               (2, lista[1], 'Pune', 18, 1, 'Raj', 'Mumbai'),
               (3, lista[0], 'Mumbai', 20, 1, 'Raj', 'Mumbai'),
               (4, lista[0], 'Mumbai', 21, 1, 'Raj', 'Mumbai'),
               (5, lista[0], 'Delhi', 21, 1, 'Raj', 'Mumbai'),
               (6, lista[0], 'Mumbai', 19, 1, 'Raj', 'Mumbai'),
               (7, lista[0], 'Pune', 18, 1, 'Raj', 'Mumbai'),
               (8, lista[0], 'Mumbai', 20, 1, 'Raj', 'Mumbai'),
               (9, lista[0], 'Mumbai', 21, 1, 'Raj', 'Mumbai'),
               (10, lista[0], 'Delhi', 21, 1, 'Raj', 'Mumbai'),
               (11, lista[0], 'Mumbai', 19, 1, 'Raj', 'Mumbai'),
               (12, lista[0], 'Pune', 18, 1, 'Raj', 'Mumbai'),
               (13, lista[0], 'Mumbai', 20, 1, 'Raj', 'Mumbai'),
               (14, lista[0] , 'Mumbai', 21, 1, 'Raj', 'Mumbai'),
               (15, lista[0], 'Delhi', 21, 1, 'Raj', 'Mumbai'),
               (16, lista[0], 'Mumbai', 19, 1, 'Raj', 'Mumbai'),
               (17, lista[0], 'Pune', 18, 1, 'Raj', 'Mumbai'),
               (18, lista[0], 'Mumbai', 20, 1, 'Raj', 'Mumbai'),
               (19, lista[0], 'Mumbai', 21, 1, 'Raj', 'Mumbai'),
               (20, lista[0], 'Delhi', 21, 1, 'Raj', 'Mumbai')]

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
