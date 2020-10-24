a = int(input("insira os dias: "))
b = int(input("insira as horas: "))
c = int(input("insira os minutos: "))
d = int(input("insira os segundos: "))
a = a * 86400
b = b * 3600
c = c * 60
x = a + b + c + d
print("o tempo em segundos é : " + str(x))