v = int(input("valor casa"))
s = int(input("salario"))
a = int(input("anos a pagar"))

if v/(a*12) > 0.3*s:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")