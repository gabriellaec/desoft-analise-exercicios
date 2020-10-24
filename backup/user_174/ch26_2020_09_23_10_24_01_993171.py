y=int(input("Qual o valor da casa?"))
s=int(input("Qual o salário?"))
z=int(input("Qual a quantidade de anos a pagar?"))
if (y/12*z)<=(30/100)*s:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")