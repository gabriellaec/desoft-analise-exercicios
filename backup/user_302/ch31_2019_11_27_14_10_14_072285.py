valor_casa = int(input("Qual valor da casa a ser comprada?"))
salario = int(input("Qual seu salário?"))
anos = int(input("Em quantos anos deseja pagar?"))
meses = anos * 12
prestacao = valor_casa/meses
if prestacao > 0.3 * salario:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")