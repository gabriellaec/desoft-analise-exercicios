d = ('deposito inicial')
t = ('taxa de juros')
m = 1
soma = 0
while(m<25):
    f = d*(1+t)**m
    m += 1
    soma += f
    print(f)
    break
else:
    print(soma)