import math
vel=int(input("velocidade:" ))
θ=int(input("graus:"))
def distância(x):
    d=(vel**2)*(math.sin(2*θ))/9.8
    if d<98:
        print ('Muito perto')
    if 98<=d<=102:
        print ('Acertou!')
    else:
        print ('Acertou!')
