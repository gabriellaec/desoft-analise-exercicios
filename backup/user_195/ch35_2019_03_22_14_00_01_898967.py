deposito=float(input("Qual o depósito inicial?"))
dm=float(input("Qual o deposito mensal?"))
juros=float(input("Qual a taxa de juros?"))
meses=1
mensal=deposito
while meses<=24:
    deposito=deposito*(1+juros)+dm
    print("{0:.2f}".format(deposito))
    meses+=1
    
retirado=deposito-mensal-24*dm
print("{0:.2f}".format(retirado))