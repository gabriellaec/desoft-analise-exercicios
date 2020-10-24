tempo = float (input("Tempo: "))
pos0 = float (input ("Posição inicial: "))
vel = float (input ("Velocidade: "))
def calcula_posicao (x,y,z):
    f = y + z*x
    return f
funcao = calcula_posicao (tempo,pos0,vel)
print (funcao)