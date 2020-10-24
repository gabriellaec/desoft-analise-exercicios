x=int(input("salario"))
y=int(input("valor da casa"))
z=int(input("anos"))
if (y/(z*12))>(x*0.3):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")