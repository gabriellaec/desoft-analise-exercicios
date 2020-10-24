def eh_crescente(lista):
    i = 1
    s = 0
    while i<len(lista):
        if lista[i] > lista[s]:
            s += 1
            return True
        else:
            return False
      