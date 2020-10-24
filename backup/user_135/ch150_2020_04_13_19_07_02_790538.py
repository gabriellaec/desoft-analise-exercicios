def calcula_pi(n):
    resultado1 = 0
    for numero in range(1, n + 1):
        pi_quadrado = 6/(numero**2)
        resultado1 += pi_quadrado
    resultado2 = (resultado1)**(1/2)
    return resultado2