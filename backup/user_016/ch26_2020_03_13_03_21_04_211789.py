valor = int(input('Qual o valor da casa a comprar? '))
salário = int(input('Qual o valor do salário? '))
tempo = int(input('Em quantos anos pretende pagar? '))
prestação_mensal = valor/tempo
if (prestação_mensal > 0.30*salário):
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')