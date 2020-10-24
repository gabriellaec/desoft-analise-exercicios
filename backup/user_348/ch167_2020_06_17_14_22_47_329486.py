def bairro_mais_custoso (bairros):
    for bairro, lista_gastos in bairros.items():
        maior_gasto = 0
        total_gastos = 0
        i = 6
        while i < 12:
            total_gastos = total_gastos + lista_gastos[i]
            if total_gastos > maior_gasto:
                maior_gasto = total_gastos
                mais_custoso = bairro
            i = i + 1
        return mais_custoso
            