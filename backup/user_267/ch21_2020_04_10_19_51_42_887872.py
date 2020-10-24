
def soma(quantia_de_dias, quantia_de_horas,quantia_de_minutos, quantia_de_segundos):
    soma1 = (quantia_de_segundos) + (quantia_de_minutos*60) +(quantia_de_horas*3600) + (quantia_de_dias*86400)
    return soma1

quantia_de_dias = int(input('Digite um número de dias:'))
quantia_de_horas = int(input('Digite um número de horas:'))
quantia_de_minutos = int(input('Digite um número de minutos:'))
quantia_de_segundos = int(input('Digite um número de segundos:'))
print(soma(quantia_de_dias,quantia_de_horas,quantia_de_minutos,quantia_de_segundos))

