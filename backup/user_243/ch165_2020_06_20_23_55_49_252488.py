def mais_populoso(pais):
    maior_estado = ""
    maior_populacao = 0
    a = 0
    
    for estado in pais:
        for municipio in pais[estado]:
            a += a + pais[estado][municipio]
        if a > maior_populacao:
            maior_populacao = a
            maior_estado = estado
    return maior_estado
            