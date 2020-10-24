def soma(x, y, w, h): 
    z=x+y+w+h
    return z
a=int(input('dias:'))
b=int(input('horas:'))
c=int(input('minutos:'))
d=int(input('segundos:'))
k=soma((a*86400),(b*3600),(c*60),d)
print(k)
