def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    
    x = lista[1] - lista[0]
    
    if x < 0:
        for i in range (len(lista) - 1):
            if lista[i] - lista[1] >= 0:
                return "nenhum"
            
    if x > 0:
        for i in range (len(lista) - 1):
            if lista[i] - lista[i + 1] <= 0:
                return "nenhum"
    
    if x > 0:
        return "crescente"
    elif x < 0:
        return "decrescente"
    elif x == 0:
        return "nenhum"