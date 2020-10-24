valor_casa=input('Qual o valor da casa')
salario=input('Qual o seu salário')
anos=('Quantos anos para pagar')

meses=anos/12

prestacao=valor_casa/meses 

porcentagem=salario*0.3

if porcentagem < prestacao:
     print('Empréstimo não aprovado')
if porcentagem>prestação or porcentagem == prestacao:
    print('Empréstimo aprovado')