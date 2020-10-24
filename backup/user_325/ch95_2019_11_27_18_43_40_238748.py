def mais_populoso(dicpopulacao, municipio):
    soma = 0
    for estado in dicpopulacao:
        soma += dicpopulacao[estado][municipio]
    return soma
