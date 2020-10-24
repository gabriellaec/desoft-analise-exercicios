
def dias(d, h, m, s):
    dia = d * 86400
    horas = h * 3600
    minutos = m * 60
    soma = dia + horas + minutos + s
    return soma


d = int(input("quantos dias"))
h = int(input("quantas horas"))
m = int(input("quantos minutos"))
s = int(input("quantos segundos"))

print(dias(d, h, m, s))