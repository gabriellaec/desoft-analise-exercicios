def mais_populoso (brasil):
    maior_populacao = 0
    mais_populoso = ''
    for estado, municípios in brasil.items():
        populacao = 0
        for habitantes in municípios.values():
            populacao = populacao + habitantes
            if populacao > maior_populacao:
                maior_populacao = populacao
                mais_populoso = estado
    return estado
