pergunta_dia = int(input ('Quantos dias? '))
pergunta_horas = int(input ('quantas horas? '))
pergunta_minutos = int (input ('Quantos minutos? '))
pergunta_segundos = int (input ('Quantos segundos? '))

tempo_seg = pergunta_segundos + (pergunta_dia * 86400) + (pergunta_horas * 3600) + (pergunta_minutos * 60)
print (tempo_seg)