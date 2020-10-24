def total_do_semestre_por_bairro(dicionario_gastos_12):
    dicionario_gastos_6 = {}
    lista_bairros = list(dicionario_gastos_12.keys())
    lista_gastos = list(dicionario_gastos_12.values())
    contador = 0

    for bairro in lista_bairros:
        dicionario_gastos_6[bairro] = lista_gastos[contador][6:12]
        contador += 1

    return dicionario_gastos_6