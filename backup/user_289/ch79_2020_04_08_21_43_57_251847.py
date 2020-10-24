def monta_dicionario(lista_keys, lista_values):
    meu_dicionario = dict ()
    i = 0
    while i < len(lista_values):
        meu_dicionario['lista_keys[i]'] = lista_values[i]
        i += 1
    return meu_dicionario


