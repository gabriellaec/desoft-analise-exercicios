v = int(input('Valor= '))
s = int(input('Salário= '))
a = int(input('Anos= '))
m = anos*12
p = v/m
if p > s*0.3:
    print('Empréstimo não aprovado')
else: 
    print('Empréstimo aprovado')