def remove_vogais (n):
    lista = [a,e,i,o,u]
    lista2 = []
    for i in n:
        if i not in lista:
            lista2.append (i)
    return lista2
            