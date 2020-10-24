casa=float(input("Valor da Casa"))
salario=float(input("Salário"))
tempo=int("Anos a pagar")
prestacao=casa/(tempo*12)
if prestacao<=0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')