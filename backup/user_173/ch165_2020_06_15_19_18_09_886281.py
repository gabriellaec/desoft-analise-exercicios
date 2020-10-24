def mais_populoso(br):
    br = {}
    maior_pop = 0
    maior_estado = ''
    for estado in br:
        i = 0
        for municipio in estado:
            i += pais[estado][municipio]
        if i > maior_pop:
            maior_pop = i
            maior_estado = estado
            
        return maior_estado