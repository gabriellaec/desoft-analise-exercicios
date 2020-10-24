valor_da_casa=int(input('Quanto custa a casa? '))
salario=int(input('Qual o valor do seu salário? '))
quantidade_anos=int(input('Quantos anos tem para pagar a sua casa? '))

prestacao=valor_da_casa/(quantidade_anos*12)

if prestacao < salario*1.30:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')