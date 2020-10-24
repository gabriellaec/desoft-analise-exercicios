d = int(input("quantidade de dias"))
h = int(input("quantidade de horas"))
m = int(input("quantidade de minutos"))
s = int(input("quantidade de segundos"))

def calcula_dias(d, h, m, s):
    dia = 86400*d
    hora = 3600*h
    minu = 60*m
    soma = dia+hora+minu+s
    return soma
print(soma)