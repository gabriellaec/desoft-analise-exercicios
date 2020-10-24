valor_casa = int(input("Qual o valor da casa?: " ))
salario = int(input("Qual o salario?:" ))
anos = int(input("Em quantos anos?: "))
meses = 12*anos
valor_prestacao = valor_casa/meses
if valor_prestacao>0.3*salario:
    print ("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")