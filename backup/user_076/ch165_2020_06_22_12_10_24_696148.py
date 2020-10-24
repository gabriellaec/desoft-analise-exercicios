def mais_populoso (brasil):
    maior_população = 0
    for estado in brasil:
        população_estadual = 0
        d_estado = brasil[estado]
        for municipio in d_estado:
            população_estadual += d_estado[município]
        if população_estadual>maior_população:
            maior_população = população_estadual
            mais_populoso = estado
    return mais_populoso
            