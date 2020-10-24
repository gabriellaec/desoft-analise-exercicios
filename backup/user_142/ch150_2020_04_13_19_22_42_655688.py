n = 1
def calcula_pi (n):
    i = 1
    r = 0
    while i - 1 < n:
        r = r + 6/(i**2)
        i = i + 1
    pi = r**1/2
    return pi
print(calcula_pi(n))
    