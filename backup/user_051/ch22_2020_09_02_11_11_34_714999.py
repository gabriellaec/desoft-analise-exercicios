c=int(input('quantos cigarros vc fuma por dia? '))
a=int(input('há quantos anos vc fuma? '))
#t=(c*365*a*10)/1536
t=(c*10*30*12*a)/1536
print (int(round(t)))