teste = float(input("Qual a distância (em km) que deseja percorrer?"))
if teste <= 200:
    print("O preço da passagem é R${0:.2f}".format(teste*0.5)
if teste > 200:
    a = ((teste-200)*0.45+100)
    print("O preço da passagem é R${0:.2f}".format(a))