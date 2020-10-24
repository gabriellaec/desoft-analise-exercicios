dias = int(input("quantos dias? "))
horas = int(input("quantas horas? "))
minutos = int(input("quantos minutos? "))
segundos = int(input("quantos segundos? "))
def segundos(dias,horas,minutos,segundos):
    y = dias*86400+horas*3600+minutos*60+segundos
    return y
print (segundos(dias,horas,minutos,segundos))