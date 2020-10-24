# pergunta a quantidade de dias
quantidade_de_dias = int (input("quantos dias?"))
#pergunta quantas horas
quantidade_de_horas = int (input("quantas horas?"))
#pergunta a quantidade de minutos
quantidade_de_minutos = int (input("quantos minutos?"))
#pergunta a quantidade de segundos
quantidade_de_segundos = int (input("quantos segundos?"))
def y( quantidade_de_dias, quantidade_de_horas, quantidade_de_minutos, quantidade_de_segundos):
    b = quantidade_de_dias * 3600 * 24 + quantidade_de_horas * 3600 + quantidade_de_minutos * 60 + quantidade_de_segundos
    return b
print (b( quantidade_de_dias, quantidade_de_horas, quantidade_de_minutos, quantidade_de_segundos))



