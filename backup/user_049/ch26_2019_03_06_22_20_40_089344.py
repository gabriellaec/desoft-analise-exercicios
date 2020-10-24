dias=input('Diga uma quantidade de dias: ')
horas=input('Diga uma quantidade de horas: ')
minutos=input('Diga uma quantidade de minutos: ')
segundos=input('Diga uma quantidade de segundos: ')
def quantidade_de_segundos(dias,horas,minutos,segundos):
    y=int(dias)*24*3600+int(horas)*3600+int(minutos)*60+int(segundos)
    return y
print (quantidade_de_segundos(dias,horas,minutos,segundos)