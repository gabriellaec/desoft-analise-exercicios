def inverte_dicionario(dicionario):
    inverte={}
    for nome,idade in dicionario.items():
        if idade not in inverte:
            inverte[idade]=[nome]
        else:
            inverte[idade].append(nome)
    return inverte