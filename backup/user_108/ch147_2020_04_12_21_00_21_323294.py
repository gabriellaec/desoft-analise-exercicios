def mais_frequente(lista):
    dicionario = {x:lista.count(x) for x in lista}
    print(max(dicionario))