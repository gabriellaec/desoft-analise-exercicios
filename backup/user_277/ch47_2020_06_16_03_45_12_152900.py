def estritamente_crescente(lista):
i = 0
lista2 = []
while i <len(lista):
    if i == 0:
        lista2.append(lista[i])
    elif lista[i-1] < lista[i]:
        lista2.append(lista[i])
    i+=1

    return lista2
        