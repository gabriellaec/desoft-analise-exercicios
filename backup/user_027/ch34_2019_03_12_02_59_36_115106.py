dep = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))/100
prod = dep
cont = 1
soma = 0
while cont <= 24:
    prod = prod*(1+tx)
    print('{:.2f}'.format(prod))
    soma = soma + prod
    cont = cont + 1
soma = soma - (100*cont)
print('{:.2f}'.format(soma))
