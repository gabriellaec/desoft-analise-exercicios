import math
g=9.8
v=float(input("diga a velocidade ?")
T=float(input("diga o angulo de lancamento?")
d=(v**2)*(math.sin(math.radians(2T)))/9.8
if(d<98):
      print('Muito perto')
elif(d>102):
      print( 'Muito longe')
else:
      print( 'Acertou!')
      