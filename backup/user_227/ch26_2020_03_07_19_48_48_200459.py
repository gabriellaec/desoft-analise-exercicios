valor_da_casa = float(input("Qual o valor da casa a comprar? "))
salário = float(input("Qual seu salário? "))
anos = int(input("Qual a quantidade de anos a pagar? "))
valor_da_prestação = (valor_da_casa/(12*anos))
if valor_da_prestação > 0.3*salário :
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
    