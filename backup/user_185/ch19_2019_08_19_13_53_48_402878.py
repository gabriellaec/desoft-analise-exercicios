import math
raiz = math.sqrt
seno = math.sin
g = 9.8
def calcula_distancia_do_projetil (v, θ ,y0 ):
    começo = (v ** 2) / (2 * g)
    meio_interno = ((2 * g * y0) /  ((v ** 2) * seno ( θ)))
    meio = 1 + raiz (1 + meio_interno)
    fim = seno ( 2 * θ )
    resultado = começo * meio * fim
    return resultado
