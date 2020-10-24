def total_do_semestre_por_bairro(dic_gastos):
    soma = 0
    lista_bairros = list(dic_gastos.keys())
    lista_gastos = list(dic_gastos.values())
    lista_ultsem = []
    for i in range(len(lista_gastos)):
        soma = lista_gastos[i][6]+lista_gastos[i][7]+lista_gastos[i][8]+lista_gastos[i][9]+lista_gastos[i][10]+lista_gastos[i][11]
        lista_ultsem.append(soma)
    novod = {}
    for i in range(len(lista_ultsem)):
        novod[lista_bairros[i]] = lista_ultsem[i]
    return novod