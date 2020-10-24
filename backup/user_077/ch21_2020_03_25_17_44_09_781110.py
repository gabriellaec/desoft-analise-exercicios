def s(a,b,c,d):	
    y=a*86400+b*3600+c*60+d
    return y
e=input('dias')
f=input('horas')
g=input('minutos')
h=input('segundos')
z= s(e,f,g,h)
print(z)