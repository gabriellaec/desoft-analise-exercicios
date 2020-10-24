def calcula_pi(n):

    pi = 0
    lista_pi = []

    for i in range(1, n + 1):
        lista_pi.append(6/i**2)
    
    pi = (sum(lista_pi)**(1/2))

    return pi