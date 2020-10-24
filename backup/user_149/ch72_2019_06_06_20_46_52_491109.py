def lista_caracteres(lista):
    
    rept = []
    
    for e in lista:
        if not e in rept:
            rept.append(e)

    return rept 
            