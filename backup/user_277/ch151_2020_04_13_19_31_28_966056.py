def classifica_lista(lista):
    if len(lista)<2:
        return "nenhum"
    
    else:
        for i in lista:
            if lista[i]<lista[i+1]:
                return "crescente"
            elif lista[i]>lista[i+1]:
                return "decrescente"
            else:
                return "nenhum"
        