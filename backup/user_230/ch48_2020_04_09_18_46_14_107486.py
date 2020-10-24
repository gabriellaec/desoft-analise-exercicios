def eh_crescente(lista):
    i=0
    while i <len(lista):
        if lista[i+1]>lista[i]:
            return True
        else:
            return False
        break
       