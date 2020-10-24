import math
raiz = math.sqrt
seno = math.sin
gravidade = 9.8
def calcula_distancia_do_projetil ( velocidade, gravidade, altura, ângulo ):
    começo = (velocidade ** 2) / (2 * gravidade)
    meio_interno = ((2 * gravidade * altura) /  ((velocidade ** 2) * seno (2 * ângulo)))
    meio = raiz (1 + meio_interno)
    fim = seno ( 2 * ângulo )
    resultado = começo * meio * fim
    return resultado
