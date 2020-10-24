dep = float(input('Qual o depósito inicial?'))
i = float(input('Qual a taxa de juros?'))
total=0
t=1
while i<=24:
    mes = (dep*(1+i)**t)
    total = total + mes
    print ('{0}:.2f'.format(mes))
    i=i+1
print ('{0}:.2f'.format(total))