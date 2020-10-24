def classifica_lista(lista):
    i=1
    lista2=[lista[0]]
    lista3=[lista[0]]
    if len(lista) < 2:
        return 'nenhum'
    w=lista[0]
    while i <len(lista):
        if lista[i] > w:
            w=lista[i]
            lista2.append(w)
        else:
            w=lista[i]
            lista3.append(w)
        i+=1
    if lista2 == lista:
        return 'crescente'
    elif lista3 == lista:
        return 'decrescente'
    else:
        return 'nenhum'
lista=[1,2,3,4,4]
q=classifica_lista(lista)
print(q)