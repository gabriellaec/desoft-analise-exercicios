def calcula_pi(n):
    dentro = 0
    for i in range(1,n+1):
        dentro += 6/(i**2)
    pi = dentro**0.5
    return pi