dep = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))
tx = tx/100
prod = dep
cont = 1
soma = 0
while cont <= 24:
    prod = prod*(1+tx)
    print('R$ {0:.2f}'.format(prod))
    soma = soma + prod
    cont = cont + 1
print('R$ {:.2f}'.format(soma))
