a = float (input("Qual o depósito inicial?"))
b = float (input("Qual a taxa de juros da poupança?"))
x = 0
while x < 24:
    y = a*b*x
    x+=1
    print ("Valor da conta com 10%: {0:.2f}".format(b))
print("{0:.2f}".format(y))
