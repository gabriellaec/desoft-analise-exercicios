salário = float(input("Diigite o valor do seu salário"))
valor_casa = float(input("Digite o valor da casa"))
anos_pagas = int(input("Digite o número de anos a pagar"))
prestação = valor_casa / (anos_pagas * 12)
if prestação > 0.3 * salário:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")