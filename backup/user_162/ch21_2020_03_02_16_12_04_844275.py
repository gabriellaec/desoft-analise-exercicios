a = int(input("Dias: "))
b = int(input("Horas: "))
c = int(input("Minutos: "))
d = int(input("Segundos: "))

print("Isso vale {} em segundos".format(d + c*60 + b*3600 + a*86400))