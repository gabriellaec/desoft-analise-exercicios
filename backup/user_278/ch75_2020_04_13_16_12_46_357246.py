def eh_primo(x): 
    if x<=1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False

    a= 3
    while a < x:
        if x%a==0:
            return False
        else:
            a += 2
    return True

def verifica_primos(l1):
    dic = {}
    for i in range (len(l1)):
        if eh_primo(l1[i]) == True:
            dic [l1[i]] = True
        else:
            dic [l1[i]] = False
    return dic