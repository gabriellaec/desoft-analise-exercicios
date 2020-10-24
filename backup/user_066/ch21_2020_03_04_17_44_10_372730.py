dia = int(input('Insira o número de dias'))
hora = int(input('Insira o número de horas'))
minuto = int(input('Insira o número de minutos'))
seg1 = int(input('Insira o número de segundos'))
def tempo_total(dia, hora, minuto, seg):
    seg2 = minuto*60
    seg3 = hora*3600
    seg4 = dia*24*3600
    tempo_total = seg1 + seg2 + seg3 + seg4
    print(tempo_total)
    return tempo_total
tempo_total(dia, hora, minuto, seg1)
    