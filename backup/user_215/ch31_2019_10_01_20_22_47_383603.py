valor = int(input("qual o valor da casa a ser comprada? "))
salario = int(input("qual o seu salario? "))
anos = int(input("em quantos anos pretende pagar? "))
prestacao = (valor/anos) / 12

if (salario * 0.3) < prestacao:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")