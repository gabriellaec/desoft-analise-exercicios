def subtracao_de_listas(lista1, lista2):
    i=0
    a=0
    b=0
    lista=[]
    while b<len(lista2):
        if lista1[i]!=lista2[a]:
            a+=1
            b+=1
        else:
            i+=1
            b+=1
    if b==a:
        lista.append(lista[i]
    else:
        i+=1
    return lista