def conta(x):
    y=(x*0.1)+x
    return y

x=float(input('quanto foi a conta seu corno? : '))
print('Valor da conta com 10%: {0:.2f}'.format(conta(x)))
    