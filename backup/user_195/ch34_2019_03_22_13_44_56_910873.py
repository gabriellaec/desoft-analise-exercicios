deposito=float(input("Qual o depósito inicial?"))
juros=float(input("Qual a taxa de juros"))
tempo=24
meses=1
total=0
while meses<=tempo:
    mensal=deposito*(1+juros)**meses
    meses+=1
    print("{0:.2f}".format(mensal))

print("{0:.2f}".format(mensal-deposito))
