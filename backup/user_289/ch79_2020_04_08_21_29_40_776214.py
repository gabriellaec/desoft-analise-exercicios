def monta_dicionario(lista_keys, lista_values):
    lista_keys = []   
    lista_values = []
    meu_dicionario = dict ()
    i = 0
    e = 0
    for i in lista_keys:
        meu_dicionario['lista_keys[i]'] = lista_values[e]
        i += 1
        e += 1
    return meu_dicionario


