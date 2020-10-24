d = int(input("quantos dias?"))
h = int(input("quantas horas?"))
m = int(input("quantos minutos?"))
s = int(input("quantos segundos?"))

d = d * 86400
h = h * 3600
result = d + h + m + s

print(result)