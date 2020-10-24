def eh_primo(x):
    divisor = 0
    if (x==2 or x==0):
        return True
    elif (x%2==0):
        while (divisor<x):
            divisor +=1
            if (x%(divisor%2==0)==0):
                return False
            else:
                return True