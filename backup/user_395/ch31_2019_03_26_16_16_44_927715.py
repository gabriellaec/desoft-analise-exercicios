a = float(input('Qual o valor da casa?'))
b = float(input('Qual o salário?'))
c = float(input('Qual a quantidade de anos a pagar?'))
p = a / c
if p > b:
    print ('Empréstimo não aprovado')
elif p < 0.3*b:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')