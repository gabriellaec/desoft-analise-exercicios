a = float(input("Qual o valor da casa que você comprar?"))
b = float(input("Qual o seu salário?"))
c = float(input("Qual a quantidade de anos a pagar"))
d = a/12*c
if d > 0.3*b:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
