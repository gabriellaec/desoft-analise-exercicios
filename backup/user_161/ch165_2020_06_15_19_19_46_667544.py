
def mais_populoso(pais):
    
    maior_estado = ""
    maior_populacao = 0

    for nome_estado, municipios in pais.items():
        contador = 0
        for municipio, populacao in municipios.items():
            contador = contador + populacao
        if contador > maior_populacao:
            maior_populacao = contador
            maior_estado = nome_estado
    
    return maior_estado