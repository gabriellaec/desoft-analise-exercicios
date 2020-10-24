valor = input("Qual o valor da casa?: ")
salario = input("Qual o seu salário?: ")
anos = input("Em quantos anos pretende pagar?: ")
meses = anos*12
prestacao = valor/meses

porc = (salario*0.3)
if prestacao > porc:
    print("Emprestimo não aprovado")
elif prestacao < porc:
    print("Emprestimo aprovado")