dep = float(input('Qual o depósito inicial?'))
taxa = float(input('Qual a taxa de juros?'))
total=0
i=1
while i<25:
    mes = (dep*(1+taxa)**i)
    total = total +mes-dep
    print (mes)
    i=i+1
print (total)