dep = float(input('Qual o depósito inicial?'))
i = float(input('Qual a taxa de juros?'))
t=1
while t<=24:
    mes = (dep*(1+i)**t)
    print ('{0:.2f}'.format(mes))
    t=t+1
print ('{0:.2f}'.format(mes-dep))