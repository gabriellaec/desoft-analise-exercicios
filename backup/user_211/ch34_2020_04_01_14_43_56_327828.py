def ehprimo(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
                
            else:
                return True

    else:
        return False
l=[]
def maior_primo_menor_que(n):
    global l
    if(ehprimo(n)==True):
        return n
    elif(ehprimo(n)==False):
        for i in range(2,n):
            if(ehprimo(i)==True):
                l.append(i)
        return (max(l))
    else:
        return -1

print(maior_primo_menor_que(12))

    