def calcula_valor_devido (valor_emprestado, número_de_meses, taxa_de_juros):
    valor_final = valor_emprestado * (1 + taxa_de_juros)**número_de_meses
    return valor_final
a = 1000
b = 2
c = 0.2
empréstimo = calcula_valor_devido(a,b,c)
print (empréstimo)
    