d=float(input('Quantos dias? '))
h=float(input('Quantas horas? '))
m=float(input('Quantos minutos? '))
s= float(input('Quantos segundos? '))
def total(d,h,m,s):
    return (d*24*60*60)+(h*60*60)+(m*60)+(s)
print(total(d,h,m,s))