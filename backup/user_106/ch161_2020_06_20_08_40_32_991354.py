def num(n):
    if n % 2 == 0:
        numer = n
    else:
        numer = n + 1
    return numer

def den(d):
    if d % 2 == 0:
        denom = d + 1
    else:
        denom = d
    return denom

def PiWallis(x):
    pipor2 = 1
    for i in range (1,x+1):
        termo = num(i) / den(i)
        pipor2 = pipor2 * termo
    return pipor2 * 2

print(PiWallis(3))