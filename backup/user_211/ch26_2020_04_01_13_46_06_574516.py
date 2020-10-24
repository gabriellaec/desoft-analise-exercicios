valorcasa=int(input("qual o valor da casa?"))
salario=int(input("quanto se ganha?"))
anos=int(input("quanto anos a pagar?"))
parcela=(valorcasa/anos)
if (parcela>=(0.3*salario)):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")