valor = float(input("Qual o valor da casa?:"))
salario = float(input("Qual o salario?:"))
quantidade_de_anos = int(input("Em quantos anos?:"))

prestacao = valor/(12*quantidade_de_anos)

if prestacao > salario*0.3:
    print("Emprestimo não aprovado")
    
else:
    print("Emprestimo aprovado")