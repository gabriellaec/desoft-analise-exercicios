depi = float(input('Qual o depósito inicial?'))
depm = float(input('Qual o depósito mensal?'))
i = float(input('Qual a taxa de juros?'))
t=1
mes=depi
while t<=24:
    mes = mes*(1+i)+depm
    print ('{0:.2f}'.format(mes))
    t=t+1
print ('{0:.2f}'.format(mes-depi-(t-1)*depm))
