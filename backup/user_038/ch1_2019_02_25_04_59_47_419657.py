def calcula_valor_devido(valor, tempo, tx_juros):
	valor_final = valor*(1 + tx_juros)^tempo
    return("O resultado da sua aplicação {0}".format(valor_final))
v = input("Valor que deseja aplicar: ")
n = input("Tempo da aplicação: ")
tx = input("Taxa de juros: ")
calcula_valor_devido(v, n, tx)