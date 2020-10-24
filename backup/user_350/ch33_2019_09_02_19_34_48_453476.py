lista = lista[0]*100
lista[0] = 1
lista[1] = 1/2
i=0
while i < 99:
    lista[i+1] = lista[i]/2
print(lista)