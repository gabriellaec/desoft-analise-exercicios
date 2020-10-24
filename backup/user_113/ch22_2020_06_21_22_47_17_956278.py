dia = int(input("Quantos cigarros vc fuma por dia?: "))
anos = int(input("Há quantos anos vc fuma?: "))

tempo = (((dia*10)/60)/24)*(anos/360)
#(dia*0,00694444)*anos

print (tempo)