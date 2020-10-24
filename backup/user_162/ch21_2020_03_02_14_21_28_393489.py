def calc_segundos(h, m, s):
    hd = 3600 * h
    md = 60 * m
    segundos = hd + md + s
    print("isso equivale a {0}".format(segundos))
    return segundos 

a = int(input("digite horas: "))
b = int(input("digite minutos: "))
c = int(input("digite segundos: "))

calc_segundos(a, b, c)