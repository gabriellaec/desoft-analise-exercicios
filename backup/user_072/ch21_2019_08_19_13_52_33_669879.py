def calcula_conta(x):
    y=x*1.1
    return y
a=float(input("Valor da conta: "))
b=calcula_conta(a)
print('valor da conta com 10%:') 
c='R${0:.2f}'.format(calcula_conta(b))
print(c)

