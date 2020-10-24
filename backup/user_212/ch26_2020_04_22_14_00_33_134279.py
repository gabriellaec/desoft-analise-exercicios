valor_casa=int(input('Qual o valor da casa'))
salario=int(input('Qual o seu salário'))
anos=int(input('Quantos anos para pagar'))

meses=anos*12

prestacao=valor_casa/meses 

porcentagem=salario*0.3

if porcentagem < prestacao:
     print('Empréstimo não aprovado')
if porcentagem>prestacao or porcentagem == prestacao:
    print('Empréstimo aprovado')