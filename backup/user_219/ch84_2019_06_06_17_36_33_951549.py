def inverte_dicionario(entrada):
    saida={}
    for nome,idade in entrada.items():
        if not idade in saida:
            nomes= [nome]
        else:
            nomes= saida[idade]
            nomes.append(nome)
        saida[idade]= nomes
    return saida
