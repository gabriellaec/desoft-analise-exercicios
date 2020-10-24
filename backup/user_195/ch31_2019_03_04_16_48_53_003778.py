valor=int(input("Qual o valor da casa?"))
salario=int(input("Qual o salário?"))
tempo=int(input("Quantos anos pra pagar?"))
valorminimo=0.3*salario
prestacao=valor/(tempo*12)
if prestacao>valorminimo:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")