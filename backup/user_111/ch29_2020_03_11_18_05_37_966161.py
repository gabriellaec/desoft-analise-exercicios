deposito=float(input("Qual o depósito inicial?"))
i=float(input("Qual a taxa de juros?"))
t=0
while t<24:
    print("O valor total é de",valor,"para o mês",t)
    print ("O ganho com juros foi",ganho)
    t +=1
    deposito=deposito*(1+i)
    valor=deposito*(1+i)
    ganho=valor-deposito