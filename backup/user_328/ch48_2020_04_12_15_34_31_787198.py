def eh_crescente(lista):
    cont = 0
    i = 1
    
    if len(lista) == 0:
        return True
    elif len(lista) == 1:
        return True
    while True:
        if lista[i] > lista[cont]:
            i += 1
            cont += 1
            if i == len(lista):
                return True 
            else:
                return False