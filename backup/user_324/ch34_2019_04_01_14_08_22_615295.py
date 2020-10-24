deposito=int(input('qual o deposito inicial: ')
taxa=float(input('qual a taxa de juros: ')
mes=0
ganho=deposito*(1+taxa)**mes
while mes<25:
	print(ganho)
	mes+=1
	