def eh_crescente(lista):
    cont = 0
    t = len(lista)
    maior = lista[0]
    if len(lista) == 1:
        return True
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