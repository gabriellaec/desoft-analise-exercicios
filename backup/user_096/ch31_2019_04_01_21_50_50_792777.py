casa = float(input('qual o valor da casa: '))
salario = float(input('qual o salario: '))
anos = float(input('quantos anos ate pagar: '))*12
prestacao = casa/anos
salario30 = salario*0.3
if prestacao > salario30:
    print('Empréstimo não aprovado')
elif salario30 > prestacao:
    print('Empréstimo aprov410ado')
