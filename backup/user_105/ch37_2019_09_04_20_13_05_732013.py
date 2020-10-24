
def lista_primo(z):
    primos=[]
    i=1    
    while len(primos)<z:
        if eh_primo(i)==True:
            primos.append(i)
        i+=1
    return primos