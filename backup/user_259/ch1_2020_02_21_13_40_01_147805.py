def calcula_valor_devido(valor_inicial):
    montante = valor_inicial*(1+taxa_de_juros)**tempo_de_aplicação
    return montante
valor = 100
taxa_de_juros = 0.05
tempo_de_aplicação = 2
m = calcula_valor_devido(valor)
print("O valor a ser pago é {0} reais".format(m))

