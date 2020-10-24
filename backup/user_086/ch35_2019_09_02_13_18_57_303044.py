dinicial=float(input('Qual o valor do depósito inicial? '))
dmensal=float(input('Qual o valor do depósito mensal? '))
juros=float(input('Qual a taxa de juros da poupança investida? '))
mes=1
saldomensal=dinicial
while mes<=24:
		saldomensal=(saldomensal*(1+juros))+dmensal
		print('saldo {1:.2f}'.format(mes,saldomensal))
		mes+=1
		saldonovo=saldomensal
ganho=saldonovo-dinicial-dmensal*23
print('O total de ganhos foi {0:.2f}'.format(ganho))