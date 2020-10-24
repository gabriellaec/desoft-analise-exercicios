def total_do_semestre_por_bairro(dici):
    nome = list(dici.keys())
    lista_gastos = list(dici.values())
    gasto_ult_semes = []
    for i in range(len(lista_gastos)):
        cont = 0
        for u in range(6,12):
            cont += lista_gastos[i][u]
        gasto_ult_semes.append(cont)
    novod = {}
    for i in range(len(gasto_ult_semes)):
        novod[nome[i]] = gasto_ult_semes[i]
    return novod