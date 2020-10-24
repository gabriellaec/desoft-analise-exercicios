def eh_crescente(lista):
    for i in range(len(lista)-1):
        if lista[i] < lista[i + 1]:
            return True
        else:
            return False
       