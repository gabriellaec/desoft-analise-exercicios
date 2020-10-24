valor=float(input('Qual o valor da casa? '))
salario=float(input('Qual o salario? '))
anos=int(input('Quantos anos? '))

prestacao=valor/(anos*12)
superior=salario*0.3

if prestacao > superior:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')