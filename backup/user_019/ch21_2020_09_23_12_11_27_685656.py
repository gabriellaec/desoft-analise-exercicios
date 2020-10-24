quantidade_dias = int(input('Quantos dias?'))
quantidade_horas = int(input('Quantas horas?'))
quantidade_minutos = int(input('Quantos minutos?'))
quantidade_segundos = int(input('Quantos segundos?'))

convds = quantidade_dias*86400
convhs = quantidade_horas*3600
convms = quantidade_minutos*60
tot = convds + convhs + convms + quantidade_segundos

print("tot")

                           