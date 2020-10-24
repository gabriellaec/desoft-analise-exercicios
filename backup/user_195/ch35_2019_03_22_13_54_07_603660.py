deposito=float(input("Qual o depósito inicial?"))
dm=float(input("Qual o deposito mensal?"))
juros=float(input("Qual a taxa de juros?"))
meses=1
mensal=deposito
while meses<=24:
    mensal=deposito(1+juros)+dm
    print("{o:.2f}".format(mensal))
    meses+=1
print("{0:.2f}".format(mensal-deposito-24*dm))