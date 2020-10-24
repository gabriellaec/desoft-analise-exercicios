def primeiras_ocorrencias(a):
    dicionario = {}
    lista = []
    lista2 = []
    for i in a:
        lista.append(i)
        print(lista)
    for e in range(0,len(a)):
        lista2.append(e)
        print(lista2)
    for n,m in zip(lista,lista2):
        if n not in dicionario.keys():
            dicionario[n]=m
    return dicionario