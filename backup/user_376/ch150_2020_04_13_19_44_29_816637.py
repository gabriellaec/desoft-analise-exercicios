def calcula_pi(n)
    i=1
    while i<=n:
        q=q+6/(i**2)
        i +=1
    pi=q**(1/2)
    return pi