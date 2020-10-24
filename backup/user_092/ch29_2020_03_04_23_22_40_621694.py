d = float(input('deposito inicial'))
t = float(input('taxa de juros'))
m = 1
soma = 0
while(m<25):
    f = d*(1+t)**m
    m += 1
    soma += f
    print(f)
else:
    print(soma)