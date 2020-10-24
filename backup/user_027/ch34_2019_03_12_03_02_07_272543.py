dep = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))
prod = dep
cont = 1
soma = 0
while cont <= 24:
    prod = prod*(1+tx)
    print('{0} -------- > RS {1:.2f}'.format(cont,prod))
    soma = soma + prod
    cont = cont + 1
soma = soma - (100*cont)
print('ganhos: RS {:.2f}'.format(soma))