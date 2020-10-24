def capitaliza(x):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ALFABETO = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if x[0] not in ALFABETO:
        i = 0
        while x[0] != alfabeto[i]:
            i += 1
        x = x[1:]
        ALFABETO[i] += x
        x = ALFABETO[i]
    return x