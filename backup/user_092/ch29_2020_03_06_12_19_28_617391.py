d = float(input('deposito inicial: '))
a = float(input('taxa de juros: '))
t = a/100
m = 1
soma = 0
lista = [0]*23
while(m<25):
    f= d*((1+t)**m)
    m += 1
    soma = lista[-1] + lista[m]
    print('{0:.2f}'.format(f))
else:
    print('{0:.2f}'.format(soma))