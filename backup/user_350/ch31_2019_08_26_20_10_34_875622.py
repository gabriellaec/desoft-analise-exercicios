x = float(input("quanto custa a casa?"))
y = float(input("quanto é o salario?"))
z = float(input("quantos anos a pagar?"))
PM = x/(12*z)
if PM <= 0.3*y:
    print ("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")
