deposito=int(input("Qual o depósito inicial?"))
juros=float(input("Qual a taxa de juros"))
meses=1
total=0
while meses<24:
    mensal=deposito*(1+juros)**i
    total=total+mensal
    meses+=1
    print("{0:.2f}".format(mensal))
print("{0:.2f}".format(mensal-deposito))
