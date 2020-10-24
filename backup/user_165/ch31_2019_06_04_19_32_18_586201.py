valor_casa = int(input("Valor da casa: "))
salario = int(input("Salario: "))
quantidade_anos = int(input("Tempo: "))
valor_prestacao = valor_casa/quantidade_anos*12
if valor_prestacao*1,3 > salario:
    print("Empréstimo não aprovado")
else valor_prestacao*1,3 <= salario:
    print("Empréstimo aprovado")