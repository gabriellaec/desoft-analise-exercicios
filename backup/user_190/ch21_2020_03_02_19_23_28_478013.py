def segundos(i,h,m,s):
    t=i*(3600*24)+h*(3600)+s+m*(60)
    return t
a=int(input('entre o primeiro termo: '))
b=int(input('entre o segundo termo: '))
c=int(input('entre o terceiro termo: '))
d=int(input('entre o quarto termo: '))
f= segundos (a,b,c,d)
print (f)