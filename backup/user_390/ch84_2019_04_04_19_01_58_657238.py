def inverte_dicionario(dicionario):
    novodict={}
    for nome, idade in dicionario.items():
        novodict[idade]=nome
    return novodict