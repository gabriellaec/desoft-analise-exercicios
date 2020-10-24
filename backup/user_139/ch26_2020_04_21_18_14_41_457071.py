valor = float (input ('Qual o valor da casa?')
salario = float (input ('Qual o seu salário?')
anos = float (input ('Qual a quantidade de anos a pagar?')
a = 0.3 * salario
b = valor / (anos / 12)
if b > a:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')