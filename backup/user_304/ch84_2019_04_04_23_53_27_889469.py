def inverte_dicionario(entrada):
    saida={}
    for nome,idade in entrada.items():
        if idade not in saida:
            saida[idade]=[nome]
        else:
            saida[idade]=[nome].append(nome)
    return saida