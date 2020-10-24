def eh_primo(num):
    if num!=0 and num!=1:
        if num%2==0:
            i=num-1
        else:
            i=num-2
        while i>1:
            if num%i!=0 and num%2!=0:
                i-=2
            else:
                return False
        return True
    else:
        return False
def primos_entre(a,b):
    lista=[]
    i=0
    if a<b:
        i=a
    else:
        i=b
    while i<=a or i<=b:
        if eh_primo(i)==True:
            lista.append(i)
        i+=1
    return lista