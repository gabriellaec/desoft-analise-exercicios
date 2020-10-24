def tempo(d,h,m,s):
    return s+60*m+60*60*h+60*60*24*d
d=int(input("Quantos dias?"))
h=int(input("Quantas horas?"))
m=int(input("Quantos minutos?"))
s=int(input("Quantos segundos?"))
print(tempo(d,h,m,s))