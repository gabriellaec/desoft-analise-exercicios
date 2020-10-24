def bairro_mais_custoso(dicionario_gastos_12):
    dicionario_gastos_6 = total_do_semestre_por_bairro(dicionario_gastos_12)
    lista_bairros = list(dicionario_gastos_6.keys())
    lista_gastos = list(dicionario_gastos_6.values())
    contador = 0
    gastos_totais = []

    for bairro in lista_bairros:
        gasto = float("{0:.2f}".format(sum(lista_gastos[contador])))
        gastos_totais.append(gasto)
        contador += 1
    return lista_bairros[gastos_totais.index(max(gastos_totais))]