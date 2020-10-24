dep = float(input("Qual o depósito inicial? "))
tx = float(input("Qual a taxa de juros? "))/100
tx = tx/100
prod = dep
cont = 0
print('R$ {:.2f}'.format(prod))
while cont < 23:
    prod = prod*(1+tx)
    print('R$ {0:.2f}'.format(prod))
    cont = cont + 1

print('R$ {:.2f}'.format(prod-100))