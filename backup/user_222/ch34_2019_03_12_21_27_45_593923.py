deposito=float(input('Qual é o deposito inicial?'))
taxa=float(input('Qual é a taxa de juros?'))
i=1
s=0
while i<25:
    ganho=deposito*(juros**i)
    i+=1
    s+=s+i
print({:.2f}.format(s))
