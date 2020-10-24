#Escreva um programa que pergunte, em sequência, uma quantidade de dias, horas, minutos e segundos para o usuário. Depois calcule o total em segundos e imprima.

#definir a funcao que calcula o total de segundos

def total_em_segundos(dias , horas , minutos , segundos):
    y=dias*86400 + horas*3600 + minutos*60 + segundos
    return y

#comandos para o usuario do programa responder

num1=int(input('Digite o numero de dias'))
num2=int(input('Digite o numero de horas'))
num3=int(input('Digite o numero de minutos'))
num4=int(input('Digite o numero de segundos'))

#funcao total_em_segundos com os argumentos num1, num2, num3 e num4

x= total_em_segundos(num1,num2,num3,num4)

#o que vai aparecer no terminal como resposta 

print('O total de segundos em {0} dias, {1} horas, {2} minutos e {3} segundos é {4}'.format(num1,num2,num3,num4,x))