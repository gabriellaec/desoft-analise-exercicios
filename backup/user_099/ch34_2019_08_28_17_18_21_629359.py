dep = float(input('Qual o depósito inicial?'))
taxa = float(input('Qual a taxa de juros?'))
total=0
for i in range(25):
    mes = (dep*(1+taxa)**i)
    total = total +mes-dep
    print (mes)
print (total)