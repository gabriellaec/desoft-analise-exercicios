valor = int(input("Qual o valor da casa que vai ser comprada?"))
salario = int(input("Qual o seu salario?"))
quantanos = int(input("Qual a quantidade de anos a pagar?"))
prestacao = valor/quantanos*12
if prestacao <= 0.3*salario:
    print ("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")

                      
                      