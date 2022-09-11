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

    for i in range(20):
        lista.append(i)
    # lista.append(x1)

    label1 = tkinter.Label(root, text="Valor Agregado: "+x1)
    canvas1.create_window(200, 230, window=label1)


button1 = tkinter.Button(text='Agregar', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

print("Frecuencia de los datos:")
print(lista)


class Table:

    def __init__(self, root):


        sumtotal=0
        for i in lista:
            sumtotal=sumtotal+i


        #FRECUENCIA ACUMULADA (Fi)
        fi = []
        fi.append(lista[0])
        for i in range(19):
            fi.append(int(fi[i])+int(lista[i+1]))
        print("Frecuencia Acumulada de los datos: ")
        print(fi)

        #hi

        hi = []
        sumfi = 0
        for i in fi:
            sumfi = sumfi + float(i)

        for i in range(20):
            hi.append(float(fi[i])/sumfi)
        print("hi de los datos:")
        print(hi)

        sumhi=0
        for i in hi:
            sumhi= sumhi + float(i)



        #HI
        Hi = []
        Hi.append(hi[0])
        for i in range(19):
            Hi.append(float(Hi[i]) + float(hi[i + 1]))
        print("Hi Acumulada de los datos: ")
        print(Hi)




        lst = [("X", "fi", 'Fi', "hi", "Hi", "%", "% acumulado"),
               (1, lista[0], fi[0], hi[0],Hi[0], 'Raj', 'Mumbai'),
               (2, lista[1], fi[1], hi[1], Hi[1], 'Raj', 'Mumbai'),
               (3, lista[2], fi[2], hi[2],Hi[2], 'Raj', 'Mumbai'),
               (4, lista[3], fi[3], hi[3], Hi[3], 'Raj', 'Mumbai'),
               (5, lista[4], fi[4], hi[4], Hi[4], 'Raj', 'Mumbai'),
               (6, lista[5], fi[5], hi[5],Hi[5], 'Raj', 'Mumbai'),
               (7, lista[6], fi[6], hi[6], Hi[6], 'Raj', 'Mumbai'),
               (8, lista[7], fi[7], hi[7], Hi[7], 'Raj', 'Mumbai'),
               (9, lista[8], fi[8], hi[8], Hi[8], 'Raj', 'Mumbai'),
               (10, lista[9], fi[9], hi[9], Hi[9], 'Raj', 'Mumbai'),
               (11, lista[10], fi[10], hi[10], Hi[10], 'Raj', 'Mumbai'),
               (12, lista[11], fi[11], hi[11], Hi[11], 'Raj', 'Mumbai'),
               (13, lista[12], fi[12], hi[12], Hi[12], 'Raj', 'Mumbai'),
               (14, lista[13], fi[13], hi[13], Hi[13], 'Raj', 'Mumbai'),
               (15, lista[14], fi[14], hi[14], Hi[14], 'Raj', 'Mumbai'),
               (16, lista[15], fi[15], hi[15], Hi[15], 'Raj', 'Mumbai'),
               (17, lista[16], fi[16], hi[16], Hi[16], 'Raj', 'Mumbai'),
               (18, lista[17], fi[17], hi[17], Hi[17], 'Raj', 'Mumbai'),
               (19, lista[18], fi[18], hi[18], Hi[18], 'Raj', 'Mumbai'),
               (20, lista[19], fi[19], hi[19], Hi[19], 'Raj', 'Mumbai'),
               ("TOTAL", sumtotal, "", sumhi, "", 'Deberia dar 100 aqui', 'nada')]

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
