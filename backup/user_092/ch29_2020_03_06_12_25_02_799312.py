d = float(input('deposito inicial: '))
a = float(input('taxa de juros: '))
t = a/100
m = 1
soma = 0
h = 0
lista = [0]*28
while(m<25):
    lista[h]= d*((1+t)**m)
    m += 1
    soma = lista[h] - lista[h-1]
    print('{0:.2f}'.format(lista[h]))
else:
    print('{0:.2f}'.format(soma))