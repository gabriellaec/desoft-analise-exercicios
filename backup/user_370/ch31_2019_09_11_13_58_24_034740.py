valor=input("Qual o valor da casa que você quer comprar?") 
salario= input("Qual se salário?")
anos=input("Quantidades de anos a pagar.")
prestacao=(valor/anos*12)
salario_30=salario*0.3
if prestacao>salario_30:
    return "Empréstimo não aprovado"
else:
    return "Empréstimo não aprovado"