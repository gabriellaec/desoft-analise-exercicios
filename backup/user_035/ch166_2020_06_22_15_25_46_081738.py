def total_do_semestre_por_bairro(dic_gastos):
    soma = 0
    lista_bairros = list(dic_gastos.keys())
    lista_gastos = list(dic_gastos.values())
    lista_ultsem = []
    for i in range(len(lista_gastos)):
        soma = 0
        for d in range(6,12):
            soma = lista_gastos[i][d]
        lista_ultsem.append(soma)
    novod = {}
    for i in range(len(lista_ultsem)):
        novod[lista_bairros[i]] = lista_ultsem[i]
    return novod