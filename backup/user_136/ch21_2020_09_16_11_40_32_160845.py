def convertor(d,h, m, s):
    w= (d*24)*60*60
    c= h*60*60
    k= m*60
    y= w+c+k+s
    return y

d= int(input('quantos dias? '))
h= int(input('quantas horas? '))
m= int(input('quantos minutos? '))
s= int(input('quantos segundos? '))
resultado= convertor(d,h, m, s)
print(resultado)