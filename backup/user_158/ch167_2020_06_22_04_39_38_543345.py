def bairro_mais_custoso(dic):
    gasto_semestral ={}
    for bairro,gastos in dic.items():
        gasto_total = 0
        for i in range(0,len(gastos)):
            gasto_total += gastos[i]
        gasto_semestral[bairro] = gasto_total
    bairro_carro =""
    maior_gasto = 0
    for bairro, gasto in gasto_semestral.items():
        if gasto > maior_gasto:
            bairro_carro = bairro
    return bairro_carro