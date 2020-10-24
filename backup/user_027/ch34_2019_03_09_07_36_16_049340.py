dep_ini = float(input("Qual o depósito inicial? __"))
tx = float(input("Qual a taxa de juros em percentual? __"))
t = 0
mont = dep_ini
while t < 24:
    print('{:.2f}'.format(mont*((1 + tx)**t)))
    t += 1