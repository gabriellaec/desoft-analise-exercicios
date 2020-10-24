def estritamente_crescente(lista):
    if len(lista) > 1:   
        l = sorted(lista)
    else: 
        return []
    