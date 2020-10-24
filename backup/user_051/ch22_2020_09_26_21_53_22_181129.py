C, A=input('quantos cigarros vc fuma por dia? há quantos anos vc fuma? ').split()
a=float(A)
c=float(C)
#t=(c*365*a*10)/1536
t=(c*10*30*12*a)/1536
print(t)