valor_da_casa = int(input("Valor da casa a ser comprada: "))
salario = int(input("Salário do indivíduo"))
anos = int(input("tempo pagando em anos"))

meses = anos*12
prestacao = valor_da_casa/meses

if prestacao > (salario*0.3):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
