def inverte_dicionario(nomes_idades):
    idades = {}
    idades_ordem = {}
    for name, age in nomes_idades.items():
        if age not in idades:
            idades[age] = [name]
        else:
            idades[age] += ['' + name]
    maior_idade = max(idades.keys())
    for k, v in idades.items():
        if k < maior_idade:
            idades_ordem[k] = v
    idades_ordem[maior_idade] = idades[maior_idade]
    return idades_ordem