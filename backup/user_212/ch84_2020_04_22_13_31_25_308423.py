def inverte_dicionario(pessoas_idades):
    saida={}
    for nome in pessoas_idades:
        if pessoas_idades[nome] not in saida:
            saida[pessoas_idades[nome]]=[nome]
        elif pessoas_idades[nome]  in saida:
            saida[pessoas_idades[nome]].append(nome)
    return saida