valor_casa = int(input("Valor da casa: "))
salario = int(input("Salário: "))
qntd_anos_a_pagar = int(input("Quantidade de anos a pagar: "))
prestacao = valor_casa/(qntd_anos_a_pagar*12)
if prestacao > 0.3*salario:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")