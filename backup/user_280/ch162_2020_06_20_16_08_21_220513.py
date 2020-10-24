def verifica_lista(lista):
    lista_par = []
    lista_impar = []
    
    i = 0
    while i < len(lista):
        if lista[i]%2 == 0:
            lista_par.append(lista[i])
        else:
            lista_impar.append(lista[i])
        i += 1
        
    if len(lista_par) == len(lista):
        y = 'par'
    elif len(lista_impar) == len(lista):
        y = 'impar'
    elif len(lista) == 0:
        y = 'misturado'
    else:
        y = 'misturado'
        
    return y