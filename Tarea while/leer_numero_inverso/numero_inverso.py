#Hacer el diagrama de flujo que lea un numero entero y positivo de cualquier numero de digitos, que calcule su numero inverso y que lo imprima con el numero leido.
print("//leer//numero//inverso")

n=int(input("Ingrese el numero que deseas invertir: "))
inverso=0

#Processing
while n>0:
    r=n%10
    inverso=inverso*10+r
    n=n//10

print("El numero inverso es: ",inverso)
