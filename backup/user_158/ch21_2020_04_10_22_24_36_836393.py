d=int(input("dias"))
h=int(input("horas"))
m=int(input("minutos"))
s=int(input("segundos"))
t=(d*86400)+(h*3600)+(m*60)+s
print(round(t,2))