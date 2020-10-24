def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num==0 or num==1:
        return False
    if num<0:
        return False
    else:
        return True
def primos_entre(a,b):
    listaprimos=[]
    for i in range(a,b+1):
        if eh_primo(i):
            listaprimos.append(i)
    return listaprimos
    