valor_casa = int(input('Informe o valor da casa: '))
salario = int(input('Informe o valor de seu salário: '))
anos = int(input('infomre em qunatos anos deve pagar: '))
meses = anos * 12
parcela = valor_casa / meses

if parcela <= salario * 1.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')