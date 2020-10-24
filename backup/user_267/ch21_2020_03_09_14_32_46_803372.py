quantia_de_dias = input('Digite um número de dias:')
quantia_de_horas = input('Digite um número de horas:')
quantia_de_minutos = input('Digite um número de minutos:')
quantia_de_segundos = input('Digite um número de segundos:')

def soma(quantia_de _segundos, quantia_de _minutos,quantia_de _horas, quantia_de_dias):
    soma = quantia_de _segundos + quantia_de _minutos*60 +quantia_de _horas*3600 + quantia_de_dias*86400
    return soma
print(soma())



