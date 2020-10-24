v=float(input('Valor da casa: '))
s=float(input('Salário: '))
a=float(input('Anos de pagamento: '))
m=v/a*12
print(m)
if m<(0.3*s):
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')