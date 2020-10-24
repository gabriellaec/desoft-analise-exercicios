def estritamente_crescente(lista):
    lista_crescente = []
    maior_valor = 0
    if not lista:
        return lista
    else:  
        for i in range(0, len(lista)): 
            print(i)          
            if lista[i] > maior_valor:
                lista_crescente.append(lista[i])
                maior_valor = lista[i]
    return lista_crescente

a = [1, 3, 2, 3, 4, 6, 5]
b = [10, 1, 2, 3]
c = [10, 15, 11, 12, 13, 14]
d = [1, 1, 2, 2, 3, 3]
e = []

print(estritamente_crescente(e))
