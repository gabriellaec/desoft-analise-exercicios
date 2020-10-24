a=float(input('Qual o valor da conta?'))
b=a-(a*0.1)
round(b,2)
print('Valor da conta com 10%: R$ X.YZ',"{:.2f}").format(b)