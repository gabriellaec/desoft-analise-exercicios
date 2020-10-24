def calcula_valor_devido (x,y,z):
    montante = x*(1+z)**y
    return montante
capital = float(input("Digite o valor emprestado."))
meses = float(input("Digite o número de meses a ser calculado."))
juros = float(input("Digite a taxa de juros"))
funcao = calcula_valor_devido (capital,meses,juros)
print("O valor a ser pago ao atribuir juros compostos, sendo o montante {0}, é {1:.2}".format (capital,funcao))