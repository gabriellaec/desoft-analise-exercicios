def inverte_dicionario(dicionario):
    novo_dicio = dict()
    for nome in dicionario:
        idade = dicionario[nome]
        if idade not in novo_dicio:
            lista = [nome]
            novo_dicio[idade] = lista
        else:
            for idades in novo_dicio:
                if idade == idades:
                    lista.append(nome)
                    novo_dicio[dicionario[nome]] = lista
    return novo_dicio
            