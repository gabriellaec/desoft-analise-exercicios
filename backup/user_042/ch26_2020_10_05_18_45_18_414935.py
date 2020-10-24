valor_casa = input('Qual o valor da casa?')
salário = input('Qual o seu salário?')
anos_pagar = input('Quantidade de anos a pagar?')

valor_prestação = valor_casa/(anos_pagar*12)
if valor_prestação > salário*0.3:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')