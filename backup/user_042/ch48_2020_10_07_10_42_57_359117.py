def eh_crescente(lista):
    i = 1
    while i < len(lista):
        if lista[i] > lista[i-1]:
            i = i + 1
            contineu
        else: 
            return False
    return True
 