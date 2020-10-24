valorcasa=float(input("qual o valor da casa?"))
salario=float(input("quanto se ganha?"))
anos=int(input("quanto anos a pagar?"))
parcela=(valorcasa/anos)
if (parcela>=(0.3*salario)):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")