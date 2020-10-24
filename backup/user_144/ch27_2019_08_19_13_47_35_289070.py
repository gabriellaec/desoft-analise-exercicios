qntCigarros = int(input("Qnts cigarros por dia: "))
anosFumando = int(input("Anos fumando: "))

totalCigarros = (anosFumando * 365)*qntCigarros
diasPerdidos = (totalCigarros * 10)/24



print(" O total de dias perdidos foi {0}".format(diasPerdidos))