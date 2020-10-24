valor = float(input('Escreva o valor da casa: '))
salario = float(input('Escreva o seu salário: '))
anos = float(input('Escreva a quantidade de anos a pagar: '))

if valor/(12*anos) > salario*0.3:
    print ('Empréstimo não aprovado')
else: 
    print ('Empréstimo aprovado')