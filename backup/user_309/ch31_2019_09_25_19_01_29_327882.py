valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salario: "))
anos = int(input("Em quantos anos quer pagar? "))
meses = anos/12
prestacao_mensal = valor/meses

if prestacao_mensal > (0.30*salario):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")