def calcula_posicao (posição_inicial, instante, velocidade):
    posição = posição_inicial + (velocidade*instante)
    return posição

a= 15
b= 2
c= 20

posição_final = calcula_posicao (a,b,c)
print (posição_final)