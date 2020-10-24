def ehprimo(n):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False
l=[]
def maior_primo_menor_que(n):
    if(ehprimo(n)==True):
        return n
    elif(ehprimo(n)==False):
        for i in range(2,n):
            if(ehprimo(i)==true):
                l.append(i)
        return max(l)
    else:
        return -1
    