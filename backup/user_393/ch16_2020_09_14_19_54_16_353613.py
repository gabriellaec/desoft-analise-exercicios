def f(x):
    y= 1.1*x
    return y

num1= float(input("Valor da conta"))
a= f(num1)
print("Valor da conta com 10%: R$ {0:.2f}".format(a))