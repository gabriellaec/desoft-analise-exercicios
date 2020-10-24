def bairro_mais_custoso (bairros):
    for bairro, lista_gastos in bairros.items():
        maior_gasto = 0
        total_gastos = 0
        i = 0
        while i < 6:
            total_gastos = total_gastos + lista_gastos[i]
            i = i + 1
            if total_gastos > maior_gasto:
                maior_gasto = total_gastos
                mais_custoso = bairro
        return mais_custoso
            