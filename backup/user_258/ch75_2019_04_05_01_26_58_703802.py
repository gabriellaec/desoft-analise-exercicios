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
def verifica_primos(numeros):
    dic={}
    for e in numeros:
        if eh_primo(e)==True:
            dic[e]=True
        else:
            dic[e]=False
    return dic
            