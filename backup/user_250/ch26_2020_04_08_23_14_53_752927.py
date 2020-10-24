a = int(input("Valor casa "))
b = int(input("Salário "))
c = int(input("Qtd de anos "))

d = b*0.3
e = c*12
f = a/e

if f>d:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")