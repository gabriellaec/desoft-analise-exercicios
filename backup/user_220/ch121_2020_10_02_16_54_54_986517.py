def subtracao_de_listas(lista1,lista2):
    novalista = []
    t = 0
    while t<len(lista1):
        if lista1[t] in lista2:
            t+=1
        else:
            novalista.append(lista1[t])
            t+=1
    return novalista