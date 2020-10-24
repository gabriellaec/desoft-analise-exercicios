def calcula_valor_devido(valor_emp, meses, juros):
    vt = (valor_emp * (1-juros)) ** meses
    return vt