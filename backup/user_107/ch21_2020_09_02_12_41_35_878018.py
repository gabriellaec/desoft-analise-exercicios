input_hours = int(input('Quantas horas?'))
input_minutes = int(input('Quantos minutos?'))
input_seconds = int(input('Quantos segundos?'))

hours_2_seconds = input_hours * 60 * 60
minutes_2_seconds = input_minutes * 60

total_seconds = hours_2_seconds + minutes_2_seconds + input_seconds

print('No intervalo de {0} horas, {1} minutos e {2} segundos tem {3} segundos'.format(input_hours, input_minutes, input_seconds, total_seconds))
