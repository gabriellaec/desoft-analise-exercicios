def mais_populoso(dicionario): 
    estados = {}
    for estado, municipios in dicionario.items(): 
        total = 0
        for municipio in municipios.values(): 
            total += municipio
        estados[estado] = total
    maior_estado = ""
    maior_populacao = 0
    for estado, populacao in estados.items():
        if populacao > maior_populacao: 
            maior_populacao = populacao maior_estado = estado
    return maior_estado