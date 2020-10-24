a = float(input('Quantos dias?'))
b = float(input('Quantas horas?'))
c = float(input('Quantos minutos?'))
d = float(input('Quantos segundos?'))

def f(a, b, c, d):
    x = a + b*60 + c*60*60 + d*24*60*60
    return x
print(f(a, b, c, d))



