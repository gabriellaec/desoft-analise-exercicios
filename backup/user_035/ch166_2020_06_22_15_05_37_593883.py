def total_do_semestre_por_bairro(dic_gastos):
    soma = 0
    lista_bairros = dic_gastos.keys()
    lista_gastos = dic_gastos.values()
    lista_ultsem = []
    for i in range(len(lista_gastos)>5):
        lista_ultsem.append(lista_gastos[i])
    novod = {}
    for i in range(len(lista_ultsem)):
        novod[lista_bairros[i]] = lista_ultsem[i]
    return novod