def calcula_pi(n):
    pi_ao_quadrado = 0
    i = 1
    while i<n:
        pi_ao_quadrado += 6/i**2
        i+=1
    pi = (pi_ao_quadrado)**(1/2)
    return pi