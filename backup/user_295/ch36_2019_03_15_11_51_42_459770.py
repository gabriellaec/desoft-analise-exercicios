
def eh_primo(n):
    resto=-1
    i=2
    while resto!=0:
        if ((i%2)!=0 or (i==2)):
            resto = (n % i)
        i=i+1
    if resto==0 and n != 2:
        result = False
    else:
        result = True 
    return result