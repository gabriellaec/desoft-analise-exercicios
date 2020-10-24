v = float(input('Qual o valor da casa?'))
sal = float(input('Qual o valor do seu salário?'))
a = int(input('Em quantos anos deseja pagar o empréstimo?)
m = a*12
pres = v/m
if pres > 0.3*sal:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')