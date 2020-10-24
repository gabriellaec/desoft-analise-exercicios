def mais_populoso (brasil):
    habitantes = {}
    for estado in brasil.keys():
        maior_populacao = 0
        populacao = 0
        for habitantes in estado.values():
            populacao = populacao + habitantes
            if populacao > maior_populacao:
                maior_populacao = populacao
                mais_populoso = estado
                return estado
