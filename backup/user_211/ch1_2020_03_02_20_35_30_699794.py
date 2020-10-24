import math
x1=float(input("Digite o valor emprestado: /n"))
y1=float(input("Digite o número de meses: /n"))
z1=float(input("Digite a taxa de juros: /n"))

def calcula_valor_devido (x,y,z):
    return x*(1+z)**y
   
print('o valor devido é/n {}'.format(calcula_valor_devido(x1,y1,z1)




