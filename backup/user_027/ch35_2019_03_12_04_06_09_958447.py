dep_ini = float(input("Qual o depósito inicial? "))
dep_mens = float(input("Qual o depósito mensal? "))
tx = float(input("Qual a taxa de juros? "))
prod = dep
cont = 1
while cont <= 24:
    prod = (prod*(1+tx)) + dep_mens
    print('{0:.2f}'.format(prod))
    cont = cont + 1
rend = prod - dep_ini - (23*dep_mens)
print('{:.2f}'.format(rend))