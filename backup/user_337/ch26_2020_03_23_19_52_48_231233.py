casa = float(input('qual o valor da casa? '))
salario = float(input('qual seu salario? '))
anos = float(input('quantos anos pretende pagar? '))

prestacao = casa/(anos*12)

if prestacao > salario*0.3:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')