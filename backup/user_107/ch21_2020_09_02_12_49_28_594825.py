input_days = int(input('Quantos dias?'))
input_hours = int(input('Quantas horas?'))
input_minutes = int(input('Quantos minutos?'))
input_seconds = int(input('Quantos segundos?'))

days_2_seconds = input_days * 24 * 60 * 60
hours_2_seconds = input_says * 60 * 60
hours_2_seconds = input_hours * 60 * 60
minutes_2_seconds = input_minutes * 60

total_seconds = hours_2_seconds + minutes_2_seconds + input_seconds

print('No intervalo de {0} dias, {1} horas, {2} minutos e {3} segundos tem {4} segundos'.format(input_days, input_hours, input_minutes, input_seconds, total_seconds))
