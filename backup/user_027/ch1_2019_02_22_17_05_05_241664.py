def valor_devido(montante, meses, juros):
    valor = montante*((1 + (juros/100))**meses)
    return valor