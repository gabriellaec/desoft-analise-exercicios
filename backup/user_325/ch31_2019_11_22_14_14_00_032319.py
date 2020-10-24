v = float(input("valor"))
s = float(input("Salario"))
t = float(input("anos a pagar"))

if v/(t*12) > s*0.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")