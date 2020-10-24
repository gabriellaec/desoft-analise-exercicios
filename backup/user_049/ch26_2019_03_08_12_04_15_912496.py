dias=input()
horas=input()
minutos=input()
segundos=input()
def quantidade_de_segundos(dias,horas,minutos,segundos):
    y=int(dias)*24*3600+int(horas)*3600+int(minutos)*60+int(segundos)
    return y
print (quantidade_de_segundos(dias,horas,minutos,segundos))