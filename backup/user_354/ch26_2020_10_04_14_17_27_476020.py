y=int(input("valor da casa"))
x=int(input("salario"))
z=int(input("anos"))
if (y/(z*12))>(x*0.3):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")