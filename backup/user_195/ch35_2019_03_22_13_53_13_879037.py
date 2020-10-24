deposito=float(input("Qual o depósito inicial?"))
dm=float(input("Qual o deposito mensal?"))
juros=float(input("Qual a taxa de juros?"))
meses=1
mensal=deposito
while meses<=24:
    mensal=deposito(1+juros)
    mensal=mensal+dm
    meses+=1
    print("{o:.2f}".format(mensal))
print("{0:.2f}".format(mensal-deposito-24*dm))