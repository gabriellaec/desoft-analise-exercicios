valor_casa=input('Qual o valor da casa')
salario=input('Qual o seu salário')
anos=('Quantos anos para pagar')

meses=anos/12

prestacao=valor_casa/meses 

porcentagem=salario*0.3

if porcentagem < prestacao:
    return False 
if porcentagem>prestação or porcentagem == prestacao:
    return True 

if False:
    print('Empréstimo não aprovado')
if True:
    print('Empréstimo aprovado')