v = input('valor: ')
s = input('salario: ')
a = input('anos: ')

m = a*12
p = v / m

if p > s*0.3:
    print('Emprésrimo não aprovado')
else:
    print('Empréstimo aprovado')