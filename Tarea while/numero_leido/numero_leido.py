print("///SUMA//DE//DIGITOS///")

# input
n=int(input("Ingresa el numero que deseas sumar: "))
#Processing
sum=0
while n>0:
    sum=sum+(n%10)
    n= n//10
print("La suma de los digitos es: ",sum)