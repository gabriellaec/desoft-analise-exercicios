deposito=int(input("Qual o depósito inicial?"))
juros=float(input("Qual a taxa de juros"))
meses=1
while meses<24:
    total=deposito*juros
    print("{:.2f}".format(total))
    meses+=1
print("{:.2f}".format(total))
