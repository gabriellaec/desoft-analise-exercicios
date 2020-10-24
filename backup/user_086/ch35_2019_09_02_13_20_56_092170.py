dinicial=float(input('Qual o valor do depósito inicial? '))
dmensal=float(input('Qual o valor do depósito mensal? '))
juros=float(input('Qual a taxa de juros da poupança investida? '))
mes=1
saldomensal=dinicial
while mes<=24:
		saldomensal=(saldomensal*(1+juros))+dmensal
		print('saldo {0:.2f}'.format(saldomensal))
		mes=mes+1
ganho=saldonovo-(dinicial+dmensal*23)
print('O total de ganhos foi {0:.2f}'.format(ganho))