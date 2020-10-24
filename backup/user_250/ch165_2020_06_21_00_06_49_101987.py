def mais_populoso(brasil):
    maior_pop = 0
    maior_estado = ''
    for estado in brasil:
        k = 0
        for municipio,pop in brasil[estado].items():
            k += pop
        if k > maior_pop:
            maior_pop = pop
            maior_estado = estado

    return maior_estado
            
            