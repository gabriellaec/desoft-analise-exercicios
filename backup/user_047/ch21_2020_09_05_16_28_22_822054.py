dia = int(input('Digite quantos dias'))
horas = int(input('Digite quantas horas'))
minutos = int(input('Digite quantos minutos'))
segundos = int(input('Digite quantos segundos'))
Resultado_dia = dia*24*60*60
Resultado_horas = horas*60*60
Resultado_minutos = minutos*60
Resultado_geral = Resultado_dia + Resultado_horas + Resultado_minutos + segundos
print(Resultado_geral)