def converte_para_segundos(dias, horas, minutos, segundos):
    total = dias*86400 + horas*3600 + minutos*60 + segundos
    return total

d = int(input("Entre com o total de dias:"))
h = int(input("Entre com as horas: "))
m = int(input("Entre com os minutos: "))
s = int(input("Entre com os segundos:"))
soma = converte_para_segundos(d, h, m, s)
print("O total de sgundos é {0} ." .format(soma))