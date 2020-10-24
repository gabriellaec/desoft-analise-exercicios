def PiWallis(x):
    i=1
    resultado=1
    while i<=x:
        if i%2==0:
            resultado*=i/(i+1)
            i+=1
        else:
            resultado*=(i+1)/i
            i+=1
    return resultado*2
              
              
              
              