a = float(input('deposito inicial: '))
b = float(input('deposito mensal: '))
c = float(input('taxa de juros: '))
t = c/100
m = 1
while(m<25):
    f= (d*((1+t)**m))+b
    print('{0:.2f}',format(f))