def calcula_pi(n):
    x = 0
    p = 0
    while x<=n:
        x+=1
        p += (6/x**2)**(1/2)
    return p