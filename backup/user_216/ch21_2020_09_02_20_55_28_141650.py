dias = int(input("Quantos dias?"))
horas = int(input("Quantas horas?"))
minutos = int(input("Quantos minutos?"))
segundos = int(input('Quantos segundos?'))

def f(a,b,c,d):
    a = dias * 24 * 60 * 60
    b = horas * 60 * 60
    c = minutos * 60
    d = segundos
    y = a + b + c + d
    return y

print(f(dias, horas, minutos , segundos))