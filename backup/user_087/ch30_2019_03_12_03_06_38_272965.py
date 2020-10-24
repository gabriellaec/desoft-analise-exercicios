import math
v = float(input())
θ = float(input())
θ = math.radians (θ)
d = (v**2)*(math.sin(2*θ))/9.8
if d < 98:
   print ('Muito perto')
elif d > 102:
   print ('Muito longe')
else:
   print ('Acertou!')
    
    