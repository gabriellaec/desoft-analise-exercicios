tempo_dia=int(input('Qual a o dia? :'))
tempo_hora=int(input('Qual a hora? :'))
tempo_minuto=int(input('Qual o minuto? :'))
tempo_seg=int(input('Qual os segundos? :'))
tempo_total=(tempo_dia*60*60*24)+(tempo_hora*60*60)+(tempo_minuto*60)+tempo_seg
print(tempo_total)
