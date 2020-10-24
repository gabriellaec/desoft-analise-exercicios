valor_da_casa = int(input('valor da casa'))
salario = int(input('salario'))
tempo = int(input('tempo em anos')) 

prestacao = valor_da_casa/(tempo*12)

if prestacao < 0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
