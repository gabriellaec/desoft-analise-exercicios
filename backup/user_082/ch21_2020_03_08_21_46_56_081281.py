dias= int(input('Escolha uma quantidade de Dias '))
horas= int(input('Escolha uma quantidade de Horas '))
minutos= int(input('Escolha uma quantidade de Minutos '))
segundos= int(input('Escolha uma quantidade de Segundos '))
def total_em_segundos(dias,horas,minutos):
    dias_para_segundos= (dias*24*60*60)
    horas_para_segundos= (horas*60*60)
    minutos_para_segundos= (minutos*60)
    return(dias_para_segundos + horas_para_segundos + minutos_para_segundos)
print(total_em_segundos(dias,horas,minutos) + segundos)
    