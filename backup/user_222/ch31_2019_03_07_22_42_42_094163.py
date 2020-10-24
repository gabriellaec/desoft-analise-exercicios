valor_casa=int(input('Qual é o valor da casa?'))
salario=int(input('Qual é o salário?'))
anos=int(input('Quantos anos?'))
prestacao=valor_casa/(anos*12)
if prestacao>0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
