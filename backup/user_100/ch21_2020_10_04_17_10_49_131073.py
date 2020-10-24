a = float(input('Quantos dias?'))
b = float(input('Quantas horas?'))
c = float(input('Quantos minutos?'))
d = float(input('Quantos segundos?'))

def f(a, b, c, d):
    x = d + c*60 + b*60*60 + a*24*60*60
    print(x)



