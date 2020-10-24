import math
n1 = float(input('Índice de refração 1: '))
n2 = float(input('Índice de refração 2: '))
a1 = float(input('Ângulo de incidência: '))
a2 = (n1*a1)/n2
print('O ângulo de refração é de {}°'.format(a2))