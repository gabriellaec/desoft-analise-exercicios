def tempo(d,h,m,s):
    d=int(input("Dias: "))
    h=int(input("Horas: "))
    m=int(input("Minutos: "))
    s=int(input("Segundos: "))
    total=86400*d+3600*h+60*m+s
    return total


