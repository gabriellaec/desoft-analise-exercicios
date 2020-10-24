valor = float(input("Qual valor da casa a comprar? "))
salario = float(input("Qual seu salario? "))
anos = float(input("Quantos anos deseja pagar? "))
prestação = valor/(anos*12)
if prestação > 0.3*salario:
    print('Empréstimo não aprovado')
elif prstação <= 0.3*salario:
    print('Empréstimo aprovado')