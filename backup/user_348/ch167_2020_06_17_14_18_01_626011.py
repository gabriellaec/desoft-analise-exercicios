def bairro_mais_custoso (bairros):
    for bairro in bairros.keys():
        maior_gasto = 0
        total_gastos = 0
        bairros[bairrro] = lista_gastos
        while i >= 6 and i <= 12:
            total_gastos = total_gastos + lista_gastos[i]
            i = i + 1
            if total_gastos > maior_gasto:
                maior_gasto = total_gastos
                mais_custoso = bairro
        return mais_custoso
            