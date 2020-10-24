pergunta_dia = input ('Quantos dias? ')
pergunta_horas = input ('quantas horas? ')
pergunta_minutos = input ('Quantos minutos? ')
pergunta_segundos = input ('Quantos segundos? ')

def dia_para_segundos (pergunta_dia):
    dia_para_segundos = pergunta_dia * 86400
		return dia_para_segundos
def hora_para_segundos (pergunta_horas):
    hora_para_segundos = pergunta_horas * 3600
    	return hora_para_segundos
def minuto_para_segundos (pergunta_minutos):
    minuto_para_segundos = pergunta_minutos * 60
    	return minuto_para_segundos
def total (dia_para_segundos, hora_para_segundos,  minuto_para_segundos):
    total = dia_para_segundos + hora_para_segundos + minuto_para_segundos + pergunta_segundos
    	return total
print (total)