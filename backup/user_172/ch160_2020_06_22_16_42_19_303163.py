import math
x = 0
erros = []
while x>=0 and x<=90:
    sen1 = math.sin(math.radians(x))
    sen2 = (4*x*(180-x))/(40500 - x*(180-x))
    erro = abs(sen2 - sen1)
    erros.append(erro)
    x=x+1
print (max(erros))
    