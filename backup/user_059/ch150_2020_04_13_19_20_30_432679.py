def calcula_pi(x):
    l = []
    for e in range(1, x+1):
        l.append(6/e**2)
    y = sum(l)**(1/2)
    return y