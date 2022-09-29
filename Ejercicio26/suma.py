# hallar la suma de los primeros 10 numeros enteros

print("--------------------------------------------------")
print("---suma--de--los--primeros--10--numeros--enteros--")
print("--------------------------------------------------")

#input

n = int(input("digite el valor de n:"))

#processing

i = 1
suma = 0
while (i<=n):
    suma = suma + i
    i = i + 1

#output

    print("la suma de los" + str(n)+ "primeros numeros es: " + str(suma))
