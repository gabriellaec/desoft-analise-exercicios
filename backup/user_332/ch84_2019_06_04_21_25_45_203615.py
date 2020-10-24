def inverte_dicionario(entrada):
    saida = {}
    for nome,idade in entrada.items():
        if not idade in saida:
            saida[idade] = nome
        else:
            saida[idade].append(nome)
            
    return saida
