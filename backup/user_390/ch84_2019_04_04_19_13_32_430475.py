def inverte_dicionario(dicionario):
    novodict={}
    for nome, idade in dicionario.items():
        if idade in novodict:
            novodict[idade].append(nome)
        else:
            novodict[idade]=[nome]
    return novodict