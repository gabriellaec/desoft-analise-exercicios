# Exercício 9 - Servidor
# Cálculo do volume da esfera

import math # Devemos importar as funções matemáticas para usar o 'pi' na equação

def calcula_volume_da_esfera(Raio):
    y=(4/3)*math.pi*(Raio**3)
    return y

a=5
b=calcula_volume_da_esfera(a)

print('O volume de uma esfera de raio {0} metros é {1} metros cúbicos'.format(a,b))