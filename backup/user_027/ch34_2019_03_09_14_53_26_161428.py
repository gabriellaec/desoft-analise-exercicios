dep_ini = float(input("Qual o depósito inicial? __"))
tx = float(input("Qual a taxa de juros?"))/100
t = 0
mont = dep_ini
tot = 0
while t < 24:
    print('{:.2f}'.format(mont*((1 + tx)**t)))
    t += 1
    tot = tot + (mont*(tx**t))
print('{:.2f}'.format(tot))