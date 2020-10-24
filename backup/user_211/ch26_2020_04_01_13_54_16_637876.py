v=float(input("qual o valor da casa?"))
s=float(input("quanto se ganha?"))
a=int(input("quanto anos a pagar?"))
parcela=(v/a)
trinta=0.3*s
if parcela>trinta:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")