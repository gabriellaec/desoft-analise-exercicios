def calcula_posicao (posição_inicial, tempo, velocidade):
    posição = posição_inicial + (velocidade*tempo)
    return posição

a= 15
b= 2
c= 20

posição_final = calcula_posicao (a,b,c)
print (posição_final)