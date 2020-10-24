def eh_primo (perg):
    if perg==1 or perg==0:
        return False
    elif perg==2:
        return True
    elif perg>1:
        if perg%2==0:
            return False
        else:
            impar=3
            invalid=True
            while invalid:
                if impar<perg and perg%impar ==0:
                    return False
                elif impar==perg:
                    return True
                    invalid=False
                impar+=2
def primos_entre(a, b):
    lista=[]
    i=0
    while i<a:
        i+=1
    if eh_primo(i):
        