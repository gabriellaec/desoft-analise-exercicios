input_days = int(input('Quantos dias?'))
input_hours = int(input('Quantas horas?'))
input_minutes = int(input('Quantos minutos?'))
input_seconds = int(input('Quantos segundos?'))

days_2_seconds = input_days * 124 * 60 * 60
hours_2_seconds = input_hours * 60 * 60
minutes_2_seconds = input_minutes * 60

total_seconds = days_2_seconds + hours_2_seconds + minutes_2_seconds + input_seconds

print(total_seconds)
