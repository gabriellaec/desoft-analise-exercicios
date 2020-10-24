def eh_crescente(x):
    i=1
    while(i<len(x)):
        if(x[i]>x[i-1]):
            i+=1
        else:
            return False
    return True