tempo=input('Agora você irá escolher um determinado periodo de tempo e eu o transformarei em segundos')
dia=int(input('Quantos dias voce escolheu?'))
hora=int(input('O numero de hora(s) escolhido(s) foi(ram)?'))
minuto=int(input('O numero de minuto(s) escolhido(s)?'))
segundo=int(input('E os segundos?'))
def Soma(dia,hora,minuto,segundo):
    Resultado=((dia*86400)+(hora*3600)+(minuto*60)+(segundo))
    return Resultado
L=Soma(dia,hora,minuto,segundo)
print('O tempo total foi de', L,'segundos')