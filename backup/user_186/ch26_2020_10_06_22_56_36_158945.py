casa=float(input("Qual o valor da casa? "))
salario=float(input("Seu salario: "))
tempo=float(input("Anos pagando: "))
prestacao=casa/(tempo*12)
if prestacao>salario*0.3:
    print ("Empréstimo não aprovado")
else :
    print ("Empréstimo aprovado")
    