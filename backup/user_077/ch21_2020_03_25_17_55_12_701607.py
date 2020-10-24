def s(a,b,c,d):	
    y=86400*a+3600*b+60*c+d
    return y
e=input('dias')
f=input('horas')
g=input('minutos')
h=input('segundos')
z=int(s(e,f,g,h))
print(z)