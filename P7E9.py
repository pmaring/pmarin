#Practica 7 - Ejericio 9 - Pedro Marin
#Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si
#riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
#últimas tiene que decir que riman un poco y si no, que no riman.

def f(a, b):
    pri = a[-3]
    seg = b[-3]
    ter = a[-2]
    cuar = b[-2]
    
    if (pri == seg):
        print("Las palabras riman.")
    elif (ter == cuar):
        print("Las palabras riman un poco")
    else:
        print("Las palabras no riman.")

palabra1 = input("Escribe la primera palabra: ")
palabra2 = input("Escribe la segunda palabra: ")
f(palabra1, palabra2)
