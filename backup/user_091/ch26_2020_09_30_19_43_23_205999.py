x=float(input('Qual o valor da sua casa a comprar: '))
y=float(input('Qual seu salário: '))
z=int(input('Qual a quantidade de anos a pagar: '))

if (x/12*z)/y <= 0.3:
    print ('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')