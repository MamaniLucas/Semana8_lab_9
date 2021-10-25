numeros=[]
i=0
while i <5:
    num = int(input("ingrese un numero: "))
    numeros.append(num)
    i+=1
invertidos = numeros[::-1]
print(numeros)
print(invertidos)