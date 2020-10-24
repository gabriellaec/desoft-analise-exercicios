valor_da_casa= int(input("Qual o valor da casa desejada?: R$ ")
salario= int(input("Qual o seu salário?: R$ ")
anos=int(input("Em quantos anos deseja pagar?: ")
         
valor_prestaçao= valor_da_casa/(anos*12)  
if valor_presataçao<(0.3*salario):
         return "Empréstimo aprovado"
else:
         return "Empréstimo não aprovado"