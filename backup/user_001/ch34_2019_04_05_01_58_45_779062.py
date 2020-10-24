C = float(input('depósito inicial: '))
I = float(input('taxa de juros: '))
t = 1
M = C
while t <= 24:
    t += 1
    M = M + M*(I/100)
    print("mês {1} foi de {0:.2f}".format(M,t))
print('total ganho foi de', M-C)