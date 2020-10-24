def verifica_numero(x):
    lista_quad_alg = []
    soma = 0
    if x < 1:
        return False
    for alg in str(x):
        a = int(alg)**int(alg)
        lista_quad_alg.append(a)
    soma = sum(lista_quad_alg)
    if soma == x:
        return True
    elif x != soma:
        return False

