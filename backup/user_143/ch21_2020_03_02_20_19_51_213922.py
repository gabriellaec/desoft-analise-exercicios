# pergunta a quantidade de dias
quantidade_de_dias = input("quantos dias?")
print (quantidade_de_dias)
#pergunta a quantidade de minutos
quantidade_de_minutos = input("quantos minutos?")
print (quantidade_de_minutos)
#pergunta a quantidade de segundos
quantidade_de_segundos = input("quantos segundos?")
print (quantidade_de_segundos)
def f( quantidade_de_dias, quantidade_de_minutos, quantidade_de_segundos):
    y = quantidade_de_dias * 3600 + quantidade_de_minutos * 60 + quantidade_de_segundos
    return y
