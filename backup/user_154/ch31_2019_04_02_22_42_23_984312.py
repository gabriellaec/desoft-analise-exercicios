valor = float(input("Custo da Casa"))
salario = float(input("Salario"))
anos = float(input("Anos"))

pres = valor

if anos != 0:
    pres = valor/(anos*12)

if salario*0.3 < pres:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")