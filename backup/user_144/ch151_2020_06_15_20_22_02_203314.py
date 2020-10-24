def classifica_lista(lista):
    if len(lista) < 2: 
        return("nenhum")
        
    elif lista == sorted(lista,reverse=True):
        return("decrescente")
        
    elif lista == sorted(lista):
        return("crescente")
        
    else:
        return("nenhum")