# Importando biblioteca da matemática
import math

# Calculando trabalho de uma função
# Força em Newtos, ângulo em graus e deslocamento em metros
def calcula_trabalho(forca, angulo_graus, deslocamento):
    angulo_radiano = (angulo_graus*math.pi)/180

    trabalho = forca*math.cos(angulo_radiano)*deslocamento

    return trabalho

teste = calcula_trabalho(50, 30, 150)
print(teste)