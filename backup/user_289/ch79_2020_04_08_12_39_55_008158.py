def monta_dicionario(lista_keys, lista_values):
    dicionario = dict ()
    for i in lista_keys:
        dicionario[k] = i
    for e in lista_values:
        dicionario[v] = e
    dicionario = {dicionario[k]:dicionario[v]}
    return dicionario