valor = int(input("Valor da casa a comprar: ")) 
salario = int(input("Salário: "))
anos = int(input("Anos a pagar: "))
prestacao = valor / anos * 12
if prestacao <  salario*(30/100):
    print ("Empréstimo aprovado")
else: 
    print ("Empréstimo não aprovado")