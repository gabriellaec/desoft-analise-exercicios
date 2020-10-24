def eh_crescente(lista): 
    for i in range len(lista):
        if lista[i] >= lista[i+1]:
            return False
        else:
            return True
                  