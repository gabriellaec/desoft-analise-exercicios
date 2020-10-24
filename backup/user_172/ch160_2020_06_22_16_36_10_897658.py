import math
x = 0
erros = []
while x>=0 and x<=90:
    sen1 = math.sin(math.degrees(x))
    sen2 = 4*x*(180-x)/(40500 - x*(180-x))
    erro = abs(sen1 - sen2)
    erros.append(erro)
    if erros[x+1] > erros[x]:
        maior = erros[x+1]
    x+=1
print (maior)
    