def mais_frequente(x):
    dicionario = {}
    lista = [0]
    for palavra in x:
        if palavra not in dicionario.keys():
            dicionario[palavra] = 1
        else:
            dicionario[palavra] +=1
    for palavra,quantidade in dicionario.items():
        if quantidade > lista[0]:
            lista[0] = palavra
    print ("{0}".format(lista[0]))