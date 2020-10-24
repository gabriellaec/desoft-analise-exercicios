numero_inicial = a
lista = []
i = 0
lista[0] = a
for e in lista
if lista[i]%2== 0:
    lista[i+1] = lista[i]/2
    lista.append(lista[i + 1])
else:
    lista[i+1]= 3*lista[i] + 1
    lista.append(lista[i + 1])