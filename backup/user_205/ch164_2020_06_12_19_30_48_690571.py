def traduz(lista,dicionario):
    trad = []
    for i in lista:
        palavra = i 
    for chave,valor in dicionario.items():
        if dicionario[chave] == palavra:
            trad.append(valor)
    return trad
            