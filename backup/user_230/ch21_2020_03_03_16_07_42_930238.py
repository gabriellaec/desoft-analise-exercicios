a=int(input("Insira uma quantidade de dias:"))
b=int(input("Insira uma quantidade de horas:"))
c=int(input("Insira uma quantidade de minutos:"))
d=int(input("Insira uma quantidade de segundos:"))
print(a, b, c, d)


def soma(a, b, c, d):
    s=a*86400+b*3600+c*60+d
    return s
s=soma(a, b, c, d)
print(s)

