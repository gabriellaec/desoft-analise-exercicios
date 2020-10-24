pergunta= int(input("Quantidade de dias?"))
pergunta1= int(input("Quantidade de horas?"))
pergunta2= int(input("Quantidade de minutos?"))
pergunta3= int(input ("Quantidade de segundos?"))


dias_para_segundos= pergunta*int(86400)
horas_para_segundos= pergunta1*int(3600)
minutos_para_segundos= pergunta2*int(60)


soma_dos_segundos= dias_para_segundos+horas_para_segundos+minutos_para_segundos+pergunta3
print(soma_dos_segundos)

