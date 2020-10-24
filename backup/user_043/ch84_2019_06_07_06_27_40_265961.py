def inverte_dicionario(dicionario):
    idade_igual = {}
    for nome,idade in dicionario.items():
        if not idade in idade_igual:
            idade_igual[idade]=[]
        idade_igual[idade].append(nome)
    return idade_igual