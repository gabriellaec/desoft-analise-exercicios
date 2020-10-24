# Programa que pergunta em sequência uma quantidade de dias, horas, minutos e segundos e transforma tudo pra segundos.
def transforma_em_segundos(d,h,m,s):
    t = d*(3600*24) + h*(3600) + m*(60) + s
    return t
a = input('Insira o valor de dias: ')
b = input('Insira o valor de horas: ')
c = input('Insira o valor de minutos: ')
e = input('Insira o valor de segundos: ')
z = transforma_em_segundos(a,b,c,e)
print (z)
