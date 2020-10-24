def mais_populoso (brasil):
    for estado in brasil.keys():
        maior_populacao = 0
        populacao = 0
        for municipio, habitantes in estado.items():
            populacao = populacao + habitantes
        if populacao > maior_populacao:
            maior_populacao = populacao
            mais_populoso = estado
            return estado
