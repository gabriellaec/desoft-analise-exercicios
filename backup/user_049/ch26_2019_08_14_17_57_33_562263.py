dia = int(input("dias:"))
hora = int(input("horas:"))
minutos = int(input("minutos:"))
segundos = int(input("segundos:"))

def calcula_segundos(dia,hora,minutos,segundos):
    total_segundos = dia*24*60*60 + hora*60*60 + minuntos*60 + segundos
    return total_segundos

print(calcula_segundos(dia,hora,minutos,segundos))