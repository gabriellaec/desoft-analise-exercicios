segundos = 0

segundos = segundos + 86400*float(input("Dias"))
segundos = segundos + 3600*float(input("Horas"))
segundos = segundos + 60*float(input("Minutos"))
segundos = segundos + float(input("Segundos"))

print("Total = {0}".format(segundos))