a = float(input('Quantos segundos?'))
b = float(input('Quantos minutos?'))
c = float(input('Quantas horas?'))
d = float(input('Quantos dias?'))

def f(a, b, c, d):
    x = a + b*60 + c*60*60 + d*24*60*60
    return x

print(f(a,b,c,d))