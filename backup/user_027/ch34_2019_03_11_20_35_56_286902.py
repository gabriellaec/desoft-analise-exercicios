dep_ini = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))
t = 0
mont = dep_ini
tot = 0
while t < 24:
    print('{:.2f}'.format(mont*((1 + tx)**t)))
    t += 1
    tot = tot + (mont*((1 + tx)**t))
print('{:.2f}'.format(tot))