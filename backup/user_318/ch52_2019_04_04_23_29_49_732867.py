def eh_crescente(x):
    i=0
    while(i<len(x)):
        if(x[i+1]>x[i]):
            i+=1
        else:
            return false
    return true