a = int(input('Quantos segundos?'))
b = int(input('Quantos minutos?'))
c = int(input('Quantas horas?'))
d = int(input('Quantos dias?'))

#Transformar em segundos
def Transformar_para_segundos(min, hor, dia):
    min = min * 60
    hor = hor * 60 * 60
    dia = dia * 24 * 60 * 60