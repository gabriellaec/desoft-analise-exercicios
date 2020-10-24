x=int(input("Qual o valor da casa?"))

y=int(input("Qual o seu salario"))

z=int(input("quantidade de anos a pagar"))
prestacao=x/z*12
if prestacao<0.3*y:
        print("Empréstimo não aprovado")
else:
    print('Empréstimo aprovado')