casa = float(input("Qual o valor da casa a ser comprada? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Quantos anos você terá para pagar? "))

if 0.3*salario >= casa/12*anos:
    print("Empréstimo Aprovado")

else:
    print("Empréstimo não aprovado")