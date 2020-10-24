def classifica_lista (lista):
    
    if len(lista)==1 or lista==[]:
        return "nenhum"
    else:
        for i in range(len(lista)-1):
            if lista[i+1] <= lista[i]:
                return "decrescente"
            elif lista[i+1]>=lista[i]:
                return "crescente"
            else:
                return "nenhum"