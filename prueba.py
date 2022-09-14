# Python program to create a table
import argparse
import tkinter
from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import re
import statistics
import matplotlib
from statistics import variance, stdev
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# Variables
fi = []
Hi = []
hi = []
porcentaje = []
porcentajeA = []
lista = []
lista_Str = []
global_contador = 0

# CREA LA VENTANA DE ENTRADA DE DATOS
root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def getSquareRoot():
    x1 = entry1.get()

    global global_contador
    global_contador += 1

    lista_Str.append(x1)
    # for i in range(20):
    #     lista.append(i)

    texto1 = str(x1)
    texto2 = str(global_contador)

    label1 = tk.Label(root, text="Contador:" + texto2 + " Valor Agregado:" + texto1)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Agregar Frecuencia', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()  # CIERRA LA VENTANA DE ENTRADA DE DATOS
lista = list(map(int, lista_Str))
print("Frecuencia de los datos:")
print(lista)


# TABLA DE FRECUENCIA
class Table:

    def __init__(self, root):

        sumtotal = 0
        sumhi = 0
        sumfi = 0
        sumaP = 0

        for i in lista:
            sumtotal = sumtotal + int(i)

        # FRECUENCIA ACUMULADA (Fi)
        fi.append(lista[0])
        for i in range(19):
            fi.append(int(fi[i]) + int(lista[i + 1]))
        print("Frecuencia Acumulada de los datos: ")
        print(fi)

        # hi

        for i in lista:
            sumfi = sumfi + float(i)

        for i in range(20):
            hi.append(float(lista[i]) / sumfi)
        print("hi de los datos:")
        print(hi)

        for i in hi:
            sumhi = sumhi + float(i)

        # HI
        Hi.append(hi[0])
        for i in range(19):
            Hi.append(float(Hi[i]) + float(hi[i + 1]))
        print("Hi Acumulada de los datos: ")
        print(Hi)

        for i in range(20):
            porcentaje.append(hi[i] * 100)
            sumaP = sumaP + porcentaje[i]

        print("EL porcentaje es de:")
        print(porcentaje)

        porcentajeA.append(porcentaje[0])
        for i in range(19):
            porcentajeA.append(porcentajeA[i] + porcentaje[i + 1])

        print("Porcentaje Acumulado")
        print(porcentajeA)
        lst = [("X", "fi", 'Fi', "hi", "Hi", "%", "% acumulado"),
               (1, lista[0], fi[0], hi[0], Hi[0], porcentaje[0], porcentajeA[0]),
               (2, lista[1], fi[1], hi[1], Hi[1], porcentaje[1], porcentajeA[1]),
               (3, lista[2], fi[2], hi[2], Hi[2], porcentaje[2], porcentajeA[2]),
               (4, lista[3], fi[3], hi[3], Hi[3], porcentaje[3], porcentajeA[3]),
               (5, lista[4], fi[4], hi[4], Hi[4], porcentaje[4], porcentajeA[4]),
               (6, lista[5], fi[5], hi[5], Hi[5], porcentaje[5], porcentajeA[5]),
               (7, lista[6], fi[6], hi[6], Hi[6], porcentaje[6], porcentajeA[6]),
               (8, lista[7], fi[7], hi[7], Hi[7], porcentaje[7], porcentajeA[7]),
               (9, lista[8], fi[8], hi[8], Hi[8], porcentaje[8], porcentajeA[8]),
               (10, lista[9], fi[9], hi[9], Hi[9], porcentaje[9], porcentajeA[9]),
               (11, lista[10], fi[10], hi[10], Hi[10], porcentaje[10], porcentajeA[10]),
               (12, lista[11], fi[11], hi[11], Hi[11], porcentaje[11], porcentajeA[11]),
               (13, lista[12], fi[12], hi[12], Hi[12], porcentaje[12], porcentajeA[12]),
               (14, lista[13], fi[13], hi[13], Hi[13], porcentaje[13], porcentajeA[13]),
               (15, lista[14], fi[14], hi[14], Hi[14], porcentaje[14], porcentajeA[14]),
               (16, lista[15], fi[15], hi[15], Hi[15], porcentaje[15], porcentajeA[15]),
               (17, lista[16], fi[16], hi[16], Hi[16], porcentaje[16], porcentajeA[16]),
               (18, lista[17], fi[17], hi[17], Hi[17], porcentaje[17], porcentajeA[17]),
               (19, lista[18], fi[18], hi[18], Hi[18], porcentaje[18], porcentajeA[18]),
               (20, lista[19], fi[19], hi[19], Hi[19], porcentaje[19], porcentajeA[19]),
               ("TOTAL", sumtotal, "", sumhi, "", sumaP, "")]

        total_rows = len(lst)
        total_columns = len(lst[0])

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 11, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# CREA LA VENTANA DE TABLA DE FRECUENCIAS
root = Tk()
root.title("TABLA DE FRECUENCIAS")
t = Table(root)
root.mainloop()  # CIERRA LA VENTANA DE TABLA DE FRECUENCIAS


# ABRE LA VENTANA DE MEDIA,MEDIANA Y MODA

def mean_calc(data_set):
    return statistics.mean(data_set)


media = mean_calc(lista)


def median_calc(data_set):
    sorted_data_set = list(sorted(data_set))
    data_set_length = len(sorted_data_set)

    if data_set_length == 1:
        median = data_set[0]
    elif data_set_length % 2 != 0:
        median = sorted_data_set[int((data_set_length) / 2)]
    else:
        median = (sorted_data_set[int(data_set_length / 2) - 1] + sorted_data_set[int(data_set_length / 2)]) / 2

    return median


median_calc(lista) == np.median(lista)
mediana = median_calc(lista)


def mode_calc(data_set):
    return max(set(data_set), key=data_set.count)


moda = mode_calc(lista)
moda == statistics.mode(lista)

height_unique = list(set(lista))
height_count = [lista.count(height) for height in height_unique]


def sample_var_calc(data_set):
    data_set_length = len(data_set)
    mean = mean_calc(data_set)
    variance = sum([(y-mean)**2 for y in data_set])/(data_set_length-1)
    return variance
# varianza = sample_var_calc(lista)
varianza=statistics.variance(lista)


def stdev(data_set):
    data_set_length = len(data_set)
    mean = mean_calc(data_set)
    variance = sum([(y - mean) ** 2 for y in data_set]) / (data_set_length - 1)
    return variance ** (1 / 2)

desviacion = stdev(lista)


stdev_range = [media-desviacion,media+desviacion]
three_stdev_range = [media-desviacion*3,media+desviacion*3]




plt.hist(lista, edgecolor='black', color='purple')
plt.axvline(media, color='red', lw=3, label=f"Media:{media}")
plt.axvline(mediana, color='yellow', lw=3, label=f"Mediana:{mediana}")
plt.axvline(moda, color='green', lw=3, label=f"Moda:{moda}")
plt.axvline(varianza, color='black', lw=3, label=f"Varianza:{varianza}")


plt.axvspan(stdev_range[0],stdev_range[1], alpha=.2, color='red',
         label=f"Desviacion Estandar:{desviacion}")

plt.axvspan(three_stdev_range[0],three_stdev_range[1], alpha=.2, color='green',
         label='Desviacion de los datos')

plt.xlabel('Indices')
plt.ylabel('Frecuencias')
plt.title('Graficas')
plt.legend()
plt.show()
