def mais_frequente(lista):
    dicionario = {x:lista.count(x) for x in lista}
    return dicionario[max(dicionario)]