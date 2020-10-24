
def PiWallis(n):
    meiopi=1
    
    for i in range (1,n):
        numerador = 2*i
        denominador = 2*i-1
        if n ==1:
            meiopi=2
        else:
            meiopi = meiopi * ((numerador*numerador)/(denominador*(denominador+2)))


    return 2*meiopi
