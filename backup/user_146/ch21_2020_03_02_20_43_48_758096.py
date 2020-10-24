def calcula_em_segundos(d,h,m,s):
    t = d*(3600*24)+h*(3600)+m*(60)+s
    return t
a=int(input('valor de d:'))
b=int(input('valor de h:'))
c=int(input('valor de m:'))
e=int(input('valor de s:'))
y=calcula_em_segundos(a,b,c,e)
print(y)