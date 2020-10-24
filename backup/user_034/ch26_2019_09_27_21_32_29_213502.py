a=int(input("Quantos dias?"))
b=int(input("Quantas horas?"))
c=int(input("Quantos minutos?"))
d=int(input("Quantos segundos?"))
trans_dias=86400*a
trans_horas=3600*b
trans_min=60*c
total=trans_dias+trans_horas+trans_min+d
print(total)