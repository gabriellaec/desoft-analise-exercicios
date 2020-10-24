def minutos_para_segundos(minutos):
    return minutos*60

def horas_para_segundos(horas):
    return minutos_para_segundos(horas*60)

def dias_para_segundos(dias):
    return horas_para_segundos(dias*24)

dias = int( input("Dias: ") )
horas = int( input("Horas: ") )
minutos = int( input("Minutos: ") )
segundos = int( input("Segundos: ") )

segundos += minutos_para_segundos(minutos)
segundos += horas_para_segundos(horas)
segundos += dias_para_segundos(dias)

print(segundos)