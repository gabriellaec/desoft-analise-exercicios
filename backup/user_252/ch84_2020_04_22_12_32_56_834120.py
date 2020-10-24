def inverte_dicionario(entrada):
    saida={}
    for nome,idade in entrada.items():
        if idade not in saida:
            saida[idade]=[nome]
        elif idade in saida:
            saida[i]+=[nome]
    return saida