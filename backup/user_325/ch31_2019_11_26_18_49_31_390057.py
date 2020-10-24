v = int(input("valor da casa"))
s = int(input("salario"))
t = int(input("tempo pra pagar"))
if v/(t*12) > s*0.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")