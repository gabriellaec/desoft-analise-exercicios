def inverte_dicionario(nomes_idades):
    idades_nomes = {}
    for nome, idade in nomes_idades.items():
        if idade not in idades_nomes:
            idades_nomes[idade] = [nome] 
        else:
            idades_nomes[idade].append(nome)
    return idades_nomes