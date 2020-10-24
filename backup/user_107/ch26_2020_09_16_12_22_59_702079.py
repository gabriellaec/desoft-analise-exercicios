price = float(input("O valor da casa?"))
salary = float(input("Qual o salário?"))
time = float(input("quantidade de anos a pagar?"))

deferments = time * 12
deferred = price / prestations

if deferred / deferments > 30/100:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
