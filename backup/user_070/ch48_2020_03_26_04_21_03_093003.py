def eh_crescente(lista1):
    x = 0
    if lista1 == []:
        lista2 = []
        return False
    else:
        n = len(lista1)
        i = 1
        a = lista1[0]
        lista2 = [a]
        while i < n:
            if lista2[x] < lista1[i]:
                lista2.append(lista1[i])
                i += 1
                x += 1
            else:
                i += 1
        if lista1 == lista2:
            return True
        else:
            return False