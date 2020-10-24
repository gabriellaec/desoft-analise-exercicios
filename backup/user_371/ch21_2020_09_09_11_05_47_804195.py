def tempo(x,y,z,u):
    t = x*86400+y*3600+z*60+u
    return t

dias = input("Digite os dias:")
horas = input("Digite as horas:")
minutos = input("Digite os minutos:")
segundos = input("Digite os segundos:")

d = int(dias)
h = int(horas)
m = int(minutos)
s = int(segundos)

total = tempo(d,h,m,s)

print("o tempo em segundos é: {0}".format(total))