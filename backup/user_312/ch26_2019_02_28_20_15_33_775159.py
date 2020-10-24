dias=input()
horas=input()
minutos=input()
segundos=input()
def tempo_total(dias, horas, minutos, segundos):
    y=dias*24*3600 + horas * 3600 + minutos * 60 + segundos
    return y
print(tempo_total(dias,horas,minutos,segundos))