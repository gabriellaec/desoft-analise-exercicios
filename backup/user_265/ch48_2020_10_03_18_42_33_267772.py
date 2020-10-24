def eh_crescente(lista):
    i = 0
    if len(lista) == 0:
        return True
    if len(lista) == 1:
        return True
    while i < len(lista)-1:
        if lista[i] < lista[i+1]-1:
            i += 1
            h = 0
            if lista[h] == lista[h+1]:
                return False
            else: 
                return True
        else:
            return False