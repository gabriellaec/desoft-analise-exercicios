def numerador(n):
    A = 1
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            A *= i*i
    else:
        for i in range(2, n+2, 2):
            if i > n:
                A *= i
            else:
                A *= i*i
    return A

def denominador(n):
    B = 1
    if n % 2 == 0:
        for i in range(1, n+2, 2):
            if i > n:
                B *= i
            else:
                B *= i*i
    else:
        for i in range(1, n+1, 2):
            B *= i*i
    return B

def PiWallis(n):
    if n == 1:
        return 2*2
    else:
        produtorio = numerador(n)/denominador(n)
        return 2*produtorio
