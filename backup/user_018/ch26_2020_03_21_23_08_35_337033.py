v = int(input('Valor= '))
s = int(input('Salário= '))
m = int(input('Meses= '))
p = v/m
if p > s*0.3:
    print('Empréstimo não aprovado')
else: 
    print('Empréstimo aprovado')