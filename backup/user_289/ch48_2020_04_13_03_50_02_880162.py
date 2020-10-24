def eh_crescente(lista): 
    for i in lista:
        if lista[i] < lista[i+1]:
            return True
        else:
            return False
                  