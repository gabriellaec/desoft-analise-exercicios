
meiopi=1.0
def PiWallis(n):
    for i in range (1,n):
        numerador = 2*i
        denominador = 2*i-1
        meiopi = meiopi * (numerador*numerador)/(denominador*(denominador+2))
    return 2*meiopi
    