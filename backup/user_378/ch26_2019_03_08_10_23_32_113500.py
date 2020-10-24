d=input('Dias:')
d=int(d)
h=input('Horas:')
h=int(h)
m=input('Minutos:')
m=int(m)
s=input('Segundos:')
s=int(s)
def calcula_seg(d,h,m,s):
    y=int(d*86400+h*3600+m*60+s)
    return y
print('o total de segundos é:',calcula_seg(d,h,m,s)