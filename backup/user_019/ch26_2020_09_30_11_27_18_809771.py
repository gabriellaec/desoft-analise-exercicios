vcasa = int(input('Qual o valor da casa? '))
salario = int(input("Qual seu salário? "))
anos = int(input("Em quantos nos você deseja pagar? "))

meses = anos* 12
prestacao = vcasa/meses
status = salario * 0.3

if status < prestacao:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")