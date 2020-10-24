import math
x=float(input("Digite o valor emprestado: /n"))
y=float(input("Digite o número de meses: /n"))
z=float(input("Digite a taxa de juros: /n"))

def calcula_valor_devido (x,y,z):
    x*(1+z)**y
print('o valor devido é/n {}' .format(calcula_valor_devido))




