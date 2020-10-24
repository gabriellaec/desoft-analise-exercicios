def calcula_pi(n):
    i = 0
    dentrodaraiz = 0
    while i < n:
        dentrodaraiz += (6/(i**2))
        i+=1
    pi = dentrodaraiz**(1/2)
    return pi