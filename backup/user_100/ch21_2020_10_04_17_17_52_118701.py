a = int(input('Quantos dias?'))
b = int(input('Quantas horas?'))
c = int(input('Quantos minutos?'))
d = int(input('Quantos segundos?'))

def f(a, b, c, d):
    x = d + c*60 + b*60*60 + a*24*60*60
    print(x)




