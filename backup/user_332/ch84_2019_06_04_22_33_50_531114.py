def inverte_dicionario(entrada):
    saida = {}
    for nome,idade in entrada.items():
        if idade in saida:
            nomes = [saida[idade]]  
            nomes.append(nome)
            saida[idade] = nomes
        else:
            saida[idade] = nome
            
    return saida