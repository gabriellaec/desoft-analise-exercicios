dias= int(input("Quantos dias? "))
horas= int(input("Quantas horas? "))
minutos= int(input("Quantos minutos? "))
segundos= int(input("Quantos segundos? "))
def conversoes(dias,horas,minutos,segundos):
    dias_seg= dias*86400
    horas_seg= horas*3600
    minutos_seg= minutos*60
    total= dias_seg + horas_seg + minutos_seg + segundos
    return total