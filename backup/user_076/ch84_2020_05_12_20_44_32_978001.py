def inverte_dicionario (nomes_idades):
    idades_nomes = {}
    for nome in nomes_idades:
        if nomes_idades[nome] not in idades_nomes:
            lista = []
            idades_nomes[nomes_idades[nome]] = lista.append(nome)
        if nomes_idades[nome] in idades_nomes:
            lista = idades_nomes[nomes_idades[nome]]
            lista.append(nome)
         
    