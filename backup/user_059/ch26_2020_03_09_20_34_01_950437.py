casa = int(input('Qual o valor da casa: R$:'))
salario = int(input('Qual O seu salário: R$:'))
tempo = int(input('Em quanto tempo pretende pagar: R$:'))

prestação = casa/tempo

if prestação>(salario*0.30):
    print('Empréstimo não aprovado')
else: 
    print('Empréstimo aprovado')