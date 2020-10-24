def mais_populoso(estado_city_popul):
    popul_por_estado = {}
    for estado, cidades in estado_city_popul.items():
        # População para cada estado
        popul_por_estado[estado] = 0
        for populacao in cidades.values():
            # Soma população das cidades na total do estado
            popul_por_estado[estado] += populacao
    for estado, populacao in popul_por_estado.items():
        if populacao == max(popul_por_estado.values()):
            return estado