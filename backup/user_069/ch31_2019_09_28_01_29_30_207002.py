valor = float(input('Qual o valor da casa?' ))
salario = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos deseja pagar? '))
prestacao = valor/tempo*12
if prestacao =< 0.3*salario:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')