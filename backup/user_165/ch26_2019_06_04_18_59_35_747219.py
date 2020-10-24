d=int(input("quantos dias?"))
h=int(input("quantas horas?"))
m=int(input("quantos minutos"))
s=int(input("quantos segundos"))
def t(d,h,m,s):
    y=(d*86400+h*3600+m*60+s)
    return y

totaldesegundos =t(d,h,m,s)
print ("O total de segundos é {0}" .format(totaldesegundos))