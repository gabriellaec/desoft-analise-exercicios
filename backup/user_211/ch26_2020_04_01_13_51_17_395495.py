v=float(input("qual o valor da casa?"))
s=float(input("quanto se ganha?"))
a=int(input("quanto anos a pagar?"))
parcela=(v/a)
if parcela>0.3*s:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")