valor_casa = float(input("Valor da Casa: "))

salario = float(input("Valor do Salário: "))

anos_pagar = float(input("Qte de Anos: "))

valor_prestacao = valor_casa / anos_pagar*12

if valor_prestacao > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')