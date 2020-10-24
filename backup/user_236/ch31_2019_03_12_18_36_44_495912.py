a=float(input("qual o valor da casa? "))
b=float(input("qual seu salario? "))
c=float(input("quantos anos para pagar"))
d=a/(12*c)
if d>0.3*b:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")