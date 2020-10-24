def inverte_dicionario(nomes_idades):
    idades = {}
    for name, age in nomes_idades.items():
        if age not in idades:
            idades[age] = [name]
        else:
            idades[age] += [' ' + name]
    return idades