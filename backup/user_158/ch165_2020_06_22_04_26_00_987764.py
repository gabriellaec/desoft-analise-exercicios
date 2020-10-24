def mais_populoso(dic):
    estados ={}
    for estado,municipios in dic.items():
        total = 0
        for municipio in municipios.values():
            total += municipio
        estados[estado] = total
    maior_pop = 0
    estado_pop =""
    for estado, populacao in estados.items():
        if populacao > maior_pop:
            maior_pop = populacao
            estado_pop = estado
    return estado_pop