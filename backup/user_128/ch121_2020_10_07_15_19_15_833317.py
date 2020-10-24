def subtracao_de_listas(lista1, lista2):
    for e in lista1:
        if e in lista2:
            lista1.remove(e)
        else:
            pass
        
    return lista1