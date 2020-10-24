dias=int(input('qual é o numero de dias? '))
horas=int(input('qual é o numero de horas? '))
minutos=int(input('qual é o numero de minutos? '))
segundos=int(input('qual é o numero de segundos? '))
def cal_segundos(dias, horas, minutos, segundos):
    y=dias*86400+horas*3600+minutos*60+segundos
    return y
print (cal_segundos(dias, horas, minutos, segundos))