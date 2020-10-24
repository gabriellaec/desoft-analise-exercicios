dep_ini = float(input("Qual o depósito inicial? "))
dep_mens = float(input("Qual o depósito mensal? "))
tx = float(input("Qual a taxa de juros? "))
juros = (1 + (tx/100))
prod = dep_ini
cont = 0
while cont < 24:
    print('{0:.2f}'.format(prod))
    prod = (prod*(1+tx)) + dep_mens
    cont = cont + 1
rend = prod - dep_ini - (23*dep_mens)
print('{:.2f}'.format(rend))