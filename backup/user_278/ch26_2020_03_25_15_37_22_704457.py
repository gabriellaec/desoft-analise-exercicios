valor_da_casa= float(input("Qual o valor da casa desejada?: R$ "))
salario = float(input("Qual o seu salário?: R$ "))
anos= float(input("Em quantos anos deseja pagar?: "))
         
valor_prestaçao= valor_da_casa/(anos*12)  

if valor_prestaçao<(0.3*salario):
    print ("Empréstimo aprovado")
else:
    print ("Empréstimo não aprovado")