valor=(float(input("Qual o valor da casa que você quer comprar? "))) 
salario= (float(input("Qual se salário? ")))
anos=int(input("Quantidades de anos a pagar. "))
prestacao=(valor/anos*12) 
salario_30=salario*0.3
if prestacao>salario_30:
    print ("Empréstimo não aprovado")
else:
    print ("Empréstimo aprovado")