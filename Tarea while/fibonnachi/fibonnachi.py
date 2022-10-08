#La serie fibonnachi es una secuencia numerica, en la cual cada elemento es igual a la suma de los dos anteriores. Tomando como variables iniciales los dos primeros elementos A= 0 y B = 1, hacer el diagrama de flujo y el programa en python, que calcule e imprima a partir del tercero, todos los elementos de la serie fibonnacci que sean menores que 1000.
print("//Serie//Fibonnachi//")

# Processing
A=0
B=1
C=A+B
while 1000>C:
    C=A+B
    A=B
    B=C
    print("el numero de la serie fibonnachi fue: ",C)
print("Fin de los numeros que eran pedidos")