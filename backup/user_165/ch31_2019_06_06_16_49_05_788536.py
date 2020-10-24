valor_casa = int(input("Valor da casa: "))
salario = int(input("Salario: "))
quantidade_anos = int(input("Tempo: "))
valor_prestacao = valor_casa/quantidade_anos*12
if (valor_prestacao > (salario*0.3)):
    print("Empréstimo não aprovado")
elif (valor_prestacao <=(salario*0.3)):
    print("Empréstimo aprovado")