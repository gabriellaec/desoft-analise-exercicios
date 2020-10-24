def inverte_dicionario(dicionario):
    dicionario2 = {}
    for nome in dicionario:
        idade = dicionario[nome]
        if idade in dicionario2:
            dicionario2[idade].append(nome)
        else:
            dicionario2[idade] = [nome]  
    return dicionario2

    