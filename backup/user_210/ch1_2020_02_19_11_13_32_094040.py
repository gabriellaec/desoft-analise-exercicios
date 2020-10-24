def calcula_valor_devido(valor, meses, taxa):
    if meses == 0:
        return valor
    return float(valor)*((1+float(taxa))^float(meses))
    