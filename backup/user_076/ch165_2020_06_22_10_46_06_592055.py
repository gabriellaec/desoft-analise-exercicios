def mais_populoso (brasil):
    for estado in brasil:
        maior_população = 0
        população_estadual = 0
        brasil[estado] = {}
        for município in estado:
            população_estadual += estado[município]
        if população_estadual > maior_população:
            mais_populoso = estado
    return mais_populoso
            