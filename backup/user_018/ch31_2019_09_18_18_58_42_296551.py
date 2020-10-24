b=0
p=0

valor_casa = float(input('Qual o valor da casa a comprar?'))
salario = float(input('Qual seu salário?'))
anos = float(input('Qual a quantidade de anos a pagar?'))

p = valor_casa/anos
b = salario*0.30
if p > b:
    print ('Empréstimo não aprovado')
else:
    print( 'Empréstimo aprovado')



