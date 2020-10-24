x=float(input('qual o valor da casa?'))
y=float(input('qual o seu salario'))
z=float(input('quantos meses a pagar?'))
p=x/z
if p > y*0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')