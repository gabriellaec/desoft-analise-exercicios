a=float(input('quantos cigarros vc fuma por dia? '))
c=float(input('há quantos anos vc fuma? '))
if a>0:
    t=(c*365*a*10)/1536
else:
    t=(a*10)/1536
#t=(c*10*30*12*a)/1536
print (t)