def calcula_valor_devido (valor_emprestado, numero_de_meses, taxa_de_juros):
    valor_devido = valor_emprestado * (1 + taxa_de_juros)**numero_de_meses
    return valor_devido

x = 2
y = 5
z = 0.7

funcao = calcula_valor_devido (x, y, z)
print (funcao)