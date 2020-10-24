def mais_populoso(dici):
    maior_estado = ''
    maior_populacao = 0
    for estado in dici:
        cont = 0
        for municipio in dici[estado]:
            cont += dici[estado][municipio]
        if cont > maior_populacao:
            maior_populacao = cont
            maior_estado = estado
    return maior_estado
