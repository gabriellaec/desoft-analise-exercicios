def soma(x, y, z, o):
    w=x+y+z+o
    return w
a =int( input("dias"))*60*60*24
b =int( input("horas"))*60*60
c=int(input("minutos"))*60
d=int(input('segundos'))
e = soma(a,b,c,d)
print(e)