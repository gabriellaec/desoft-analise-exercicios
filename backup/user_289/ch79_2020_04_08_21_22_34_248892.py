def monta_dicionario(lista_keys, lista_values):
    lista_keys = []   
    lista_values = []
    meu_dicionario = dict ()
    i = 0
    e = 0
    while i < len(lista_keys):
        dicionario_key = lista_keys[i]
        dicionario_value = lista_values[e]
        meu_dicionario[dicionario_key] = dicionario_value
        i += 1
        e += 1
    return meu_dicionario