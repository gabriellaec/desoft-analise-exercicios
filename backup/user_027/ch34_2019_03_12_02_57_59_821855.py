dep = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))
prod = dep
cont = 0
soma = 0
while cont <= 24:
    prod = prod*(1+tx)
    print('{:.2f}'.format(prod))
    soma = soma + prod
    cont = cont + 1
print('{:.2f}'.format(soma))
