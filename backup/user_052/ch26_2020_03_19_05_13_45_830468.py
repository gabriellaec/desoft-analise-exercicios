casa = int(input("Qual o valor da casa a comprar?\n"))
salario = int(input("Qual o salario?\n"))
anos = int(input("Qual a quantidade de anos para pagar?\n"))
meses = anos * 12
prestação = casa/meses
if prestação > salario *0.3:
    print ("Empréstimo não aprovado")
else:
    print ("'Empréstimo aprovado")