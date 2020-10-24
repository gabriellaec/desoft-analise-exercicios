def primos_entre(a,b):
    primos=[]
    i = a    
    while i<=b:
        if eh_primo(i) == True:
            primos.append(i)
        i+=1
    return len(primos)