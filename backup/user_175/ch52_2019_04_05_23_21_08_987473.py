def eh_crescente(lista):
    if len(lista) == 1:
        return True
    if len(lista) == 0:
        return True
    cont = 0
    t = len(lista)
    maior = lista[0]
    
    i = 1
    while i < t:
        if lista[i] > maior:
            maior = lista[i]
            cont += 1
        i += 1
        
    if (cont + 1) == t:
        return True
    else:
        return False