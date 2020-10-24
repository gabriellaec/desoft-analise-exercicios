def calcula_segundos(d, h, m ,s):
    d *= 86400
    h *= 3600
    m *= 60
    
    return d + h + m + s

print(calcula_segundos(int(input("Dias: ")),int(input("Horas: ")), int(input("Minutos: ")), int(input("Segundos: "))))