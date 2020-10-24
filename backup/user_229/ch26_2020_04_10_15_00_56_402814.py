valor = float(input("Qual o valor da casa? "))
anos = int(input("Quantos anos a pagar? "))
salário = float(input("Qual o seu salário? "))
prestação = valor/anos*12
if prestação > 0.3*salário:
    print('Empréstio não aprovado')
else:
    print('Empréstimo aprovado')