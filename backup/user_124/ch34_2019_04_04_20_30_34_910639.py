C = float(input("qual o depósito inicial? : "))
i = float(input("qual a taxa de juros? : "))

mes = 1
while mes <= 24:
    M = C*(1+i)**mes
    print("{0:.2f}".format(M))
    mes += 1

J = M - C
print("{0:.2f}".format(J))
