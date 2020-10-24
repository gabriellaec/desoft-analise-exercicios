valor_da_casa=float(input('Quanto custa a casa? '))
salario=float(input('Qual o valor do seu salário? '))
quantidade_anos=int(input('Quantos anos tem para pagar a sua casa? '))

prestacao=valor_da_casa/quantidade_anos*12

if prestacao < salario*1.3:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')