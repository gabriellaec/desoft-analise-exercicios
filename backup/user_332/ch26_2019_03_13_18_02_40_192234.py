def dias_horas_minutos_para_segundos(dias,horas,minutos,segundos):
    total = ((dias * 24)*60*60) + (horas*60*60) + (minutos*60) + (segundos)
    return(total)
dias = int(input("Numero de dias "))
horas = int(input("Numero de horas "))
minutos = int(input("Numero de minutos "))
segundos = int(input("Numero de segundos "))

print(dias_horas_minutos_para_segundos(dias,horas,minutos,segundos))