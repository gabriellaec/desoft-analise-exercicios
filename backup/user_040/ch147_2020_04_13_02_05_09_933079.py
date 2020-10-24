def mais_frequente(x):
    dicionario = {}
    lista = [0]
    lista2 = [0]
    for palavra in x:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] += 1
    for palavra,quantidade in dicionario.items():
        if quantidade > lista[0]:
            lista[0] = quantidade
            lista2[0] = palavra
    print (lista2)