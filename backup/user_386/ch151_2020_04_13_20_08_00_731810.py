def classifica_lista(lista1):
    if len(lista1) < 2:
        return ("nenhum")
    elif sorted(lista1) == lista1:
        return ("crescente")
    elif sorted(lista1, reverse=True) == lista1:
        return ("decrescente")
    else:
        return ("nenhum")
     
    
    