def calcula_conta(x):
    y=x*1.1
    return y
a=int(input("Valor da conta: "))
print 
b=calcula_conta(a)
print('valor da conta com 10%:') 
c=float('{0:.2f}'.format(b))
print(c)