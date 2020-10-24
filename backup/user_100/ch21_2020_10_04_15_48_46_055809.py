a = int(input('Quantos segundos?'))
b = int(input('Quantos minutos?'))
c = int(input('Quantas horas?'))
d = int(input('Quantos dias?'))

def f(a, b, c, d):
    x = a + b*60 + c*60*60 + d*24*60*60
    return x

