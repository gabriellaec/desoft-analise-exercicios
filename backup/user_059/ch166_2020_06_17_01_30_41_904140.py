def total_do_semestre_por_bairro(dici):
    nome = list(dici.keys())
    lista_gastos = list(dici.values())
    gasto_ult_semes = []
    for i in range(len(lista_gastos)):
        print(lista_gastos[i][5])
        gasto_ult_semes.append(lista_gastos[i][5]+lista_gastos[i][6]+lista_gastos[i][7]+lista_gastos[i][8]+lista_gastos[i][9]+lista_gastos[i][10]+lista_gastos[i][11])
    novod = {}
    for i in range(len(gasto_ult_semes)):
        novod[nome[i]] = gasto_ult_semes[i]
    return novod