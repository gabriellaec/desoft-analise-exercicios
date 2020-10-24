def calcula_total_em_segundos(dias, horas, minutos, segundos):
    d = (((int(dias) * 24) * 60) * 60)
    h = ((int(horas) * 60) * 60)
    min = (int(minutos) * 60)
    s = int(segundos)
    total = d + h + min + s
    print(total)

dias = input('Quantos dias? ')
horas = input('Quantos horas? ')
minutos = input('Quantos minutos? ')
segundos = input('Quantos segundos? ')