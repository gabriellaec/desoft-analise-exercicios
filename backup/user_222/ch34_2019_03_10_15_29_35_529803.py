deposito=input('Qual é o deposito inicial?')
taxa=input('Qual é a taxa de juros?')
i=1
while i<25:
    ganho=deposito*(juros**i)
    print({:.2f}.format(ganho))
    i+=1
