# pergunta a quantidade de dias
quantidade_de_dias = input("quantos dias?")
#pergunta quantas horas
quantidade_de_horas = input("quantas horas?")
#pergunta a quantidade de minutos
quantidade_de_minutos = input("quantos minutos?")
#pergunta a quantidade de segundos
quantidade_de_segundos = input("quantos segundos?")
print (quantidade_de_dias, quantidade_de_horas, quantidade_de_minutos, quantidade_de_segundos
def f( quantidade_de_dias, quantidade_de_horas, quantidade_de_minutos, quantidade_de_segundos):
    y = quantidade_de_dias * 3600 * 24 + quantidade_de_horas * 3600 + quantidade_de_minutos * 60 + quantidade_de_segundos
    return y