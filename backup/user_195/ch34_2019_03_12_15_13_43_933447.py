deposito=int(input("Qual o depósito inicial?"))
juros=float(input("Qual a taxa de juros"))
meses=1
total=0
while meses<24:
    mensal=deposito*juros
    total+=mensal
    meses+=1
    print("{:.2f}".format(total))
print("{:.2f}".format(total))
