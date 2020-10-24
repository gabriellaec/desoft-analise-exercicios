def mais_populoso(dicionario):
    estados = {}
    for estado, municipio in dicionario.items():
        total = 0
        for municipio in municipio.values():
            total += municipio
        estados[estado] = total
    maior_estado = ""
    maior_populacao = 0
    for estado, populacao in estados.items():
        if populacao > maior_populacao:
            maior_estado = estado
    return maior_estado