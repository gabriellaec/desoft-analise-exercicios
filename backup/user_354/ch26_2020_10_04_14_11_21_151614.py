x=int(input("salario"))
y=int(input("valor da casa"))
z=int(input("anos"))
if (y/(z*12))>(x*0.3):
    return("emprestimo não aprovado")
else:
    return("emprestimo aprovado")