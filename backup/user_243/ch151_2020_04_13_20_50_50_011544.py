def classifica_lista(lista):
    if len(lista)<2:
        return "nenhum"
    lista=[]
    lista1=[]
    a=0
    b=1
    while i<len(lista):
        if lista[a]<lista[b]:
            lista.append(lista[a])
        if lista[a]>lista[b]:
            lista1.append(lista[a])
        else:
            return "nenhum"
    a+=1
    b+=1
    if lista==lista1:
        return "decrescente"
    if lista==lista2:
        return "crescente"