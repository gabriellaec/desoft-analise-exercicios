def eh_crescente(lista):
    i = 0
    while i < len(lista):
        i += 1
        if lista[i] > lista[i+1]:
            return False
        if lista[i] < lista[i+1]:
            return True
        if lista[i] == lista[i+1]:
            return False
        
