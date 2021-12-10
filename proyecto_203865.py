# Sistemas empotrados - Proyecto final
# Diana Estefanía Castro Aguilar - 203865
import tkinter

import serial
from tkinter import *
from tkinter import messagebox


def leeComando():

    ventana = tkinter.Tk()
    ventana.geometry("400x300")

    texto = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()

    etiqueta = tkinter.Label(ventana, text="Circuito - Termo inteligente")
    etiqueta.pack()

    etiqueta2 = tkinter.Label(ventana, text="Temperatura")
    etiqueta2.pack()

    temperatura = tkinter.Label(ventana, textvariable= texto)
    temperatura.pack()

    etiqueta3 = tkinter.Label(ventana, text="Nivel de agua")
    etiqueta3.pack()

    nivel = tkinter.Label(ventana, textvariable= texto2)
    nivel.pack()

    etiqueta4 = tkinter.Label(ventana, text="¿Desea calentar el termo?")
    etiqueta4.pack()

    calentar = tkinter.Entry(ventana)
    calentar.pack()

    etiquetaCalentar = tkinter.Label(ventana, textvariable=texto3)
    etiquetaCalentar.pack()



    temp = None
    niv = None
    status = None
    arduino = serial.Serial('/dev/cu.usbserial-1420', 9600, timeout=5)
    while True:

        valores = arduino.readline().decode()

        a = valores.split(":")

        if len(a) == 2:
            label = a[0]
            value = a[1]

            if label == 'tem':
                temp = value
                texto.set(temp)
                print("Temperatura: ", temp)

            if label == 'niv':
                niv = value
                texto2.set(niv)
                print("Nivel de líquido: ", niv)


        if temp and niv:
            estado = True

            confirmacion = str(input('¿Desea calentar su termo?: '))

            if estado == True:
                if confirmacion == "on":
                    arduino.write(b"on")
                    print("Calentando\n")
                    status = "Calentando\n"
                    texto3.set(status)
                elif confirmacion == "off":
                    arduino.write(b"off")
                    print("No calentando\n")
                    status = "No calentando\n"
                    texto3.set(status)

                temp = None
                niv = None

            elif estado == False:
                arduino.write(b'Apagar')
                break

        ventana.update_idletasks()
        ventana.update()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    leeComando()
