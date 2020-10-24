def calcula_pi(n):
    pi= []
  
    for i in len(n):
        pi.append((6 / n ** 2)**(1/2))

    pi_2= sum(pi)

    return pi_2