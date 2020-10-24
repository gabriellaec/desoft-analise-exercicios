casa = int(input('Qual o valor da casa: R$:'))
salario = int(input('Qual O seu salário: R$:'))
tempo = int(input('Em quanto tempo pretende pagar: '))

prestação = casa/(tempo*12)

if prestação<=(salario*0.30):
    print('Empréstimo aprovado')
else: 
    print('Empréstimo não aprovado')