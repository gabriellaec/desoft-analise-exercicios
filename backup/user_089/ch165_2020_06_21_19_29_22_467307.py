def mais_populoso(pais):
    maior = 0 
    estado_maior = ""
    for estado,estados in pais.items():
        pop = 0
        for populacao in estados.values():
            pop += populacao
        if pop > maior:
            maior = pop
            estado_maior = estado
    return estado_maior