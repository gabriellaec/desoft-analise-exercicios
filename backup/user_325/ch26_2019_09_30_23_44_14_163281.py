def total(d, h, m, s):
    d = 86400*s
    h = 3600*s
    m = 60*s
    soma = d+h+m+s
    return soma

d = int(input("quantidade de dias"))
h = int(input("quantidade de horas"))
m = int(input("quantidade de minutos"))
s = int(input("quantidade de segundos"))

print(total(d, h, m, s)