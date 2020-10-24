casa = float(input("Qual o valor da casa? "))
sal = float(input("Qual o seu salário? "))
anos = float(input("Pagar em quantos anos? "))

prest = casa/(anos*12)

if prest > sal*.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")