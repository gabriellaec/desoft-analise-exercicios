def eh_primo(x):
    if(x == 0 or x == 1 or x == -1):
        return(False)
    if (x == 2 and x == - 2):
        return(True)
    if (x%2 == 0):
        return(False)
    
    a = 3
    while a < x:
        if x%a ==0:
            return(False)
        else:
            a = a + 2
    return(True)

lista = []
def primos_entre(a,b):
    lista = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            lista.append(i)
    print(sorted(lista))
    return(sorted(lista))