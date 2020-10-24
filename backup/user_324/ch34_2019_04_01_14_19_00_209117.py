deposito=int(input('qual o deposito inicial: '))
taxa=float(input('qual a taxa de juros: '))
mes=1
while mes<24:
    ganho=deposito*(1+taxa)**mes
    print(ganho)
    mes+=1
print(ganho)
	