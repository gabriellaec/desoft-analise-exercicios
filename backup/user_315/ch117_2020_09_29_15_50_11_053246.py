import math

def snell_descartes(x,y,z):

    teta2 = (x/y)*z
    return math.radians(teta2)

n1 = float(input('Insira o valor de N1: '))

n2 = float(input('Insira o valor de N2: '))

teta1 = int(input('Insira o valor de Teta1: '))

tetarad = math.radians(teta1)

print ('Convertendo Teta1 para radianos, temos: {0}'.format(tetarad))

print (snell_descartes(n1,n2,tetarad))
