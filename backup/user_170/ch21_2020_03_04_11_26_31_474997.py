import math

d = 'Entre com os dias: '
h ='Entre com as horas: ' 
m ='Entre com os minutos: '
s ='Entre com os segunds: '

def calc_segundos(d,h,m,s):
    z = (d*24*60*60)+(h*60*60)+(m*60)+(s)
    return z

print(calc_segundos(float(d),float(h),float(m),float(s)))

