def calcula_valor_devido(emp,meses,taxa):
    valor_devido = emp*((1+taxa)**meses)
    return valor_devido