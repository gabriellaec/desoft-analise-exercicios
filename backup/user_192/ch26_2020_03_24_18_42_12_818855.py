v = int(input('valor: '))
s = int(input('salario: '))
a = int(input('anos: '))

m = a*12
p = v/m

if p > s*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')