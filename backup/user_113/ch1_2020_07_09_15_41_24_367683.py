def calcula_valor_devido(valor_emp, meses, juros):
    vt = (valor_emp * juros) ** meses
    return vt