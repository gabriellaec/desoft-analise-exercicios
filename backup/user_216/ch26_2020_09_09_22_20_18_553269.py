a = float(input("Casa"))
b = float(input("Salário"))
c = int(input("Anos"))

if (a / (c * 12)) > 0.3 * b:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")