txt = float(input("Quantitade de dias: "))
txt_1 = float(input("Quantitade de horas: "))
txt_2 = float(input("Quantitade de minutos: "))
txt_3 = float(input("Quantitade de segundos: "))

total_em_horas = (txt * 24) + txt_1
total_em_minutos = (total_em_horas * 60) + txt_2
total_em_segundos = (total_em_minutos * 60) + txt_3

print(total_em_segundos)