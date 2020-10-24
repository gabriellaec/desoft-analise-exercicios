valor_casa = int(input('Qual o valor da casa a comprar?'))
salario = int(input('Qual seu salário?'))
anos = int(input('Qual a quantidade de anos a pagar?'))

p = valor_casa/(anos*12)
b = salario*0.30
if p > b:
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
   