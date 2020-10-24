def inverte_dicionario(nomes_idades):
    idades_nomes = {}
    for nome, idade in nomes_idades.items():
        if idade not in idades_nomes:
            lista = []
            idades_nomes[idade] = lista 
            lista.append(nome)
        else:
            lista.append(nome)
    return idades_nomes