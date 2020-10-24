d=input("Quantos dias?")
h=input("Quantos horas")
m=input("Quantos minutos?")
s=input("Quantos segundos?")

a=86400*int(d)
b=3600*int(h)
c=60*int(m)

y=a+b+c+int(s)
print(y)
