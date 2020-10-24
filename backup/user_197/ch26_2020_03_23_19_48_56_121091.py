valor=float(input("Qual o valor da casa?"))
salario=float(input("Qual é o salário"))
anos=int(int("Qual é a quantidade de anos a pagar?"))
prestacao=valor/(12*anos)

if prestacao<0.3*salario:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")