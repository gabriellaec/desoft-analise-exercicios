def mais_populoso(dic):
    max_pop = 0
    estado_com_max_pop = 0
    for nome in brasil:
        pop_estado = 0
        estado = brasil[nome]
        for cidade in estado:
            pop_estado += estado[cidade]
        if pop_estado > max_pop:
            max_pop = pop_estado
            estado_com_max_pop = nome
    return estado_com_max_pop