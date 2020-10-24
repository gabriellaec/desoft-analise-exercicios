def verifica_lista(lista):
    lista1=[]
    lista2=[]
    for i in lista:
        if i%2==0:
            lista1.append(i)
        if i%2!=0:
            lista2.append(i)
    if lista2==[]:
        return 'par'
    if lista1==[]:
        return 'ímpar'
    else:
        return 'misturado'