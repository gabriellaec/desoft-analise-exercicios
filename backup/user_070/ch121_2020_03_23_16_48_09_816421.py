def subtracao_de_listas(lista1,lista2):
    lista = []
    a = len(lista1)
    b = len(lista2)
    x = 0
    while x < a:
        c = 0
        y = 0
        while y < b:
            if lista1[x]!=lista2[y]:
                c += 1
                y += 1
            else:
                y += 1
        if b == c:
            lista.append(lista1[x])
            x += 1
        else:
            x += 1
    return lista