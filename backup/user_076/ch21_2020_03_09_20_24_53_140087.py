a = float(input("Dias:"))
b = float(input ("Horas:"))
c = float(input ("Minutos:"))
d = float(input ("Segundos:"))

def transforma_em_segundos (d,h,m,s):
    y = ((d*24 + h)*60 + m)*60+s
    return y

print(transforma_em_segundos(a,b,c,d))
