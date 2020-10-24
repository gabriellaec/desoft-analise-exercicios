def calcula_pi (n):
    i=1
    t=0
    while i<=n:
        a = (6/i**2)
        i=i+1
        t = t + a
    return t