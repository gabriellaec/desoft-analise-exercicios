valor_casa=int(input('Qual o valor da sua casa? '))
salario=int(input('Qual o seu salário? '))
qnt_anos=int(input('Em quantos anos você deseja efetuar o pagamento? '))
prestacao_mensal=valor_casa/(12*qnt_anos)
if prestacao_mensal <=(0.3*salario):
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')