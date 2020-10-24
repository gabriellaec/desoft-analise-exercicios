dia=input("Quantos dias? ")
hora=input("Quantas horas? ")
minuto=input("Quantos minutos? ")
segundo=input("Quantos segundos? ")
total_de_segundos=segundo+minuto*60+hora*60**2+dia*24*60**2
print(total_de_segundos)