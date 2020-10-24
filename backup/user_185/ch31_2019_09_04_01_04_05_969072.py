salário = int(input("Diigite o valor do seu salário"))
valor_casa = int(input("Digite o valor da casa"))
anos_pagas = float(input("Digite o número de anos a pagar"))
prestação = valor_casa / (anos_pagas * 12)
if prestação > 0.3 * salário:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")