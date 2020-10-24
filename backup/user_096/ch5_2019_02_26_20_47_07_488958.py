def primos(p):
    if p%2==0:
		return False
    elif p%3==0:
        return False
    elif p%5==0:
        return False
    elif p%7==0:
        return False
    elif p%11==0:
        return False
    elif p==2:
        return True
    elif p==3:
        return True
    elif p==5:
        return True
    elif p==7:
        return True
    elif p==11:
        return True
    else:
        return True




def maior_primo_menor_que(n):
    if n<0:
        return -1
    elif primos(n)==False:
        while primos(n)==False:
            n = n-1
            
        