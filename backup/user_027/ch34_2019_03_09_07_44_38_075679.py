dep_ini = float(input("Qual o depósito inicial? __"))
tx = float(input("Qual a taxa de juros em percentual? __"))
t = 1
mont = dep_ini
while t <= 24:
    print('{:.2f}'.format(mont*((1 + tx)**t)))
    t += 1
    tot = (mont - 100) + (mont*((1 + tx)**t) - 100)
print('{:.2f}'.format(tot))