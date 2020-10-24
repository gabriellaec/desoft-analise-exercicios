def calcula_pi(n):
    count = 1
    nsqrt = 0
    while (count != n):
        nsqrt = nsqrt + 6/(count**2)
        count +=1
    pi = nsqrt**0.5
    return pi
