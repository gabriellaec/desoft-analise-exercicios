dep = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))
prod = dep
cont = 1
while cont <= 24:
    prod = prod*(1+tx)
    print('{0:.2f}'.format(prod))
    cont = cont + 1
print('{:.2f}'.format(prod-dep))