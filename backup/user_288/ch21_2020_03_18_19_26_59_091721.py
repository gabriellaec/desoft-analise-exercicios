pergunta_dia = input ('Quantos dias? ')
pergunta_horas = input ('quantas horas? ')
pergunta_minutos = input ('Quantos minutos? ')
pergunta_segundos = input ('Quantos segundos? ')

def dia_para_segundos (pergunta_dia):
    dia_para_segundo = pergunta_dia * 86400
		return dia_para_segundo
def hora_para_segundos (pergungta_horas):
    hora_para_segundos = pergunta_horas * 3600
    	return hora_para_segundos
def minuto_para_segundo (pergunta_minuto):
    minuto_para_segundo = pergunta_minuto * 60
    	return minuto_para_segundo
def total (dia_para_segundo, hora_para_segundos,  minuto_para_segundo):
    total = dia_para_segundo + hora_para_segundos + minuto_para_segundo + pergunta_segundos
    	return total
print (total)