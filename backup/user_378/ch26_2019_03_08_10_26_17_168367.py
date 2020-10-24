d=int(input('Dias:'))
h=int(input('Horas:'))
m=int(input('Minutos:'))
s=int(input('Segundos:'))
def calcula_seg(d,h,m,s):
    y=int(d*86400+h*3600+m*60+s)
    return y
print('o total de segundos é:',calcula_seg(d,h,m,s))