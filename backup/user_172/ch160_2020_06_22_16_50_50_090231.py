import math
x = 0
erros = []
for x in range (91):
    sen1 = math.sin(math.radians(x))
    sen2 = (4*x*(180-x))/(40500 - x*(180-x))
    erro = abs(sen2 - sen1)
    erros.append(erro)
    if erro == max(erros):
        maior = x
print (maior)
    