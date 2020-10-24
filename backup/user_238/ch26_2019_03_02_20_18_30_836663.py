def quantidade_segundos(dias,horas,minuto,segundo):
        total=dias*86400+horas*3600+minutos*60+segundos
        return total

dias=int(input('defina uma quantidade de dias: '))
horas=int(input('defina uma quantidade de horas: '))
minutos=int(input('defina uma quantidade de minutos: '))
segundos=int(input('defina uma quantidade de segundos: '))
      
variavel=quantidade_segundos(dias,horas,minutos,segundos)  
print(variavel)