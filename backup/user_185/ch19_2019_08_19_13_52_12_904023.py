import math
raiz = math.sqrt
seno = math.sin
gravidade = 9.8
def calcula_distancia_do_projetil (v, θ ,y0 ):
    começo = (v ** 2) / (2 * gravidade)
    meio_interno = ((2 * gravidade * y0) /  ((v ** 2) * seno ( θ)))
    meio = raiz (1 + meio_interno)
    fim = seno ( 2 * θ )
    resultado = começo * meio * fim
    return resultado
