def calcula_valor_devido(valor_emp, meses, taxa_juros):
    y = valor_emp*(1+taxa_juros)**meses
    return y
valor_emp = 1000
meses = 6
taxa_juros = 0,12
a = calcula_valor_devido (valor_emp, meses, taxa_juros)
print (a)