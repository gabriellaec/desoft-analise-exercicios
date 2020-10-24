import math 
d= 100
g= 9,8
v= int(input('qual a velocidade'))
θ= int(input('qual o ângulo de lançamento'))
jw=d==str((2**v)*(2*(math.sin(θ))))/g
return jw
if jw==100:
    print ('você acertou')
elif jw<100:
    print ('você errou')
else:
    print ('você acertou')