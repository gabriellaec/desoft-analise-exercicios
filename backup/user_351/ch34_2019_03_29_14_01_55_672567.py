DI = float(input("qual o deposito inicial? "))
TJ = float(input("qual a taxa de juros da poupança? "))
n = 1
mes = 0
while n <=24:
    mes = DI*(1 + TJ)**n
    print ("{0:.2f}".format(mes))
    n+=1
print ("{0:.2f}".format(mes-DI))