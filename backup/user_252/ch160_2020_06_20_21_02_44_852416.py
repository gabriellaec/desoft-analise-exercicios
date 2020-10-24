import math
x=0
while x<=90:
    sinx=4*x*(180-x)/40500-x*(180-x)
    y=sinx-math.sin(x)
    x+=1
    print('O angulo: '.abs(y))
