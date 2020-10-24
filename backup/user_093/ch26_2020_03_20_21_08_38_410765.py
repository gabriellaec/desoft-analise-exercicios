casa=int(input('Qual o valor da casa? '))
salario=int(input('Qual o seu salario? '))
anos=int(input('Quantos anos pretende pagar? '))

prestação=casa/(anos*12)

if prestação>(salario*0.3):
    print ('Empréstimo não aprovado')

else:
    print ('Emprestimo Aprovado')