
        

def verifica_primos(primeras):
    p=primeras
    if p==2 or p==3 and p==5 or p==7 or p==11 or p==13:
        return "True"
    if p%2!=0 and p%3!=0 and p%5!=0 and p%7!=0 and p%11!=0 and p%13!=0:
        return "True"
    else:
        return "False"