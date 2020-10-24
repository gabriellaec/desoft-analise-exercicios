valor = int(input("Qual valor da casa a comprar? "))
salario = int(input("Qual seu salario? "))
anos = int(input("Quantos anos deseja pagar? "))
prestação = valor/(anos/12)
if prestação > 0.3*salario:
    print('Empréstimo não aprovado')
elif prstação <= 0.3*salario:
    print('Empréstimo aprovado')