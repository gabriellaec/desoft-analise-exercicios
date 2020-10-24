def calcula_valor_devido(valor_emprestado, taxa_juros, meses):
	valor_final = valor_emprestado * (taxa_juros**meses)
	return valor_final

ve = float(input("Insira o valor emprestado: "))
tj = float(input("Insira o valor da taxa de juros: ")) #como deixar a taxa em porcentagem??
m = float(input("Insira a quantidade de meses: "))
vf = calcula_valor_devido(ve, tj, m)

print ("O valor final devido é de {} reais".format(vf))