def filtra_positivos(lista):
    
    nova_lista = []
    
    for i in lista:
        if i > 0: nova_lista.append(i)
            
    return nova_lista