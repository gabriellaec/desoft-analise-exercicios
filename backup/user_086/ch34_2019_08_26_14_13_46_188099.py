deposito=float(input('Qual foi o depósito inicial? '))
juros=float(input('Qual é a taxa de juros da poupança? '))
mes=1
while mes<=24:
	ganho=deposito*juros**mes
	print(deposito+ganho)
    deposito=deposito+ganho
	mes+=1
ganhototal=deposito*juros**24
print('O total ganho no período foi de {0:.2f} reais'.format(ganhototal))