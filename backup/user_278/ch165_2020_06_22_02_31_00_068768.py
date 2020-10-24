def mais_populoso(dicionario):
    #cria dicionario com os estados para calcular o valor total de hab de cada estado
    estados = {}
    for estado, municipios in dicionario.items():
        total = 0
        for municipio in municipios.values():
            #soma o nº de habitantes dos estados
            total += municipio
        #atribui o valor de hab para cada estado
        estados[estado] = total
    maior_estado = ''
    maior_populacao = 0
    for estado, populacao in estados.items():
        if populacao > maior_populacao:
            maior_populacao = populacao
            maior_estado = estado
    return maior_estado