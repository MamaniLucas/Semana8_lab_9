numeros =[]
suma=0
n=int(input("Ingrese el valor de n:"))
for i in range (n):
    mi_numero =int(input("ingrese numero: "))
    numeros.append(mi_numero)
suma=0
cont=0
while cont < n:
    suma += numeros[cont]
    cont +=1
promedio=suma/len(numeros)
print("la suma es: ", suma)
print("el promedio es:", promedio)
print("El mayor es:",max(numeros))
print("El mayor es:",min(numeros))






