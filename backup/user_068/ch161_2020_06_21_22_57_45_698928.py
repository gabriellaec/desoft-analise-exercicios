
def PiWallis (n):
    conta = 1
    num = 2
    den = 1
    for i in range(n):
        a *= num/den
        if i % 2 == 0:
            den += 2
        else:
            num += 2
        i += 1
    return a * 2