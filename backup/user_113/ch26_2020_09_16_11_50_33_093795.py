valor = int(input('Qual o valor da casa?: '))
sal = int(input('Qual o seu salário?: '))
anos = int(input('Em quantos anos pagará?: '))
meses = anos/12

presta = valor/meses
if presta >= sal*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')