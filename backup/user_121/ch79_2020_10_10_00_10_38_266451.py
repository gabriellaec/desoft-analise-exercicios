def monta_dicionario(chaves, valores):
    dicionario={}
    for i in len(chaves):
        dicionario={chaves: valores}[i]
    return dicionario