

def eh_primo(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False


def maior_primo_menor_que(x):
    l=[]
    if eh_primo(x)==True:
        return x
    if eh_primo(x)==False:
        if x<2:
            return -1
        else:
            for i in range(2,x):
                if eh_primo(i)==True:
                    l.append(i)
            return max(l)
                     
                
               