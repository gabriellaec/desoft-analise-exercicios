import math
v=int(input("diga a velocidade ?")
T=int(input("diga o angulo de lancamento?")
g=9.8
d=(v**2)*math.sin(2T)/9.8
if(d<98):
      print('Muito perto')
elif(d>102):
      print( 'Muito longe')
else:
      print( 'Acertou!')
      