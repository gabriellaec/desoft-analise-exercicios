def inverte_dicionario(dicionario):
    novodic = {}
    for nome in dicionario:
        idade = dicionario[nome]
        if idade in novodic:
            novodic[idade].append(nome)
        else:
            novodic[idade]=nome
    return novodic