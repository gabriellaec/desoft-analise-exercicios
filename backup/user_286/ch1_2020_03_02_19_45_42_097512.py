def calcula_valor_devido (valor, meses, taxa):
    if meses != 0 and valor != 0 and taxa != 0:
        valor_devido = (valor * ((1 + taxa) ** meses))
        return valor_devido

