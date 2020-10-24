def soma_valores(lista1, lista2):
    lista = []
    a = len(lista1)
    b = len(lista2)
    x = 0
    while x<a:        
        lista.append(lista1[x])
        x+=1
    y = 0
    while y<b:
        lista.append(lista[y])
        y+=1
    return lista