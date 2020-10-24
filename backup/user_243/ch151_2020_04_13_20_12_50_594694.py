def classifica_lista(lista):
    if lista==[] or len(lista)==1:
        return "nenhum"
    i=0
    a=1
    while i<len(lista):
        if lista[i]<lista[a]:
            return "crescente"
        if lista[i]>lista[a]:
            return "decrescente"
        else:
            return "nenhum"
    i+=1
    a+=1