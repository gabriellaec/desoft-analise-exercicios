import math 
d= 100
g= 9,8
v= int(input('qual a velocidade'))
θ= int(input('qual o ângulo de lançamento'))
jw=d==((2**str(v))*(2*(math.sin(θ))))/g
if jw==100:
    print ('você acertou')
elif jw<100:
    print ('você errou')
else:
    print ('você acertou')