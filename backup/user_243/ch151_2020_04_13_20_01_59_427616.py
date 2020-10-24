def classifica_lista(lista):
    if lista==[] or len(lista)==1:
        return "nenhum"
    i=0
    a=1
    while i<len(lista)-1:
        if lista[i+a]<lista[i]:
            return "decrescente"
        if lista[i+a]>lista[i]:
            return "crescente"
        else:
            return "nenhum"
        i+=1
        a+=1