vc = float(input("Insira o valor da casa: "))
s = float(input("Insira o salario: "))
qa = int(input("quantos anos para pagar?: "))
pm = (vc/(qa/12))
if pm > s*0.3:
	print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")