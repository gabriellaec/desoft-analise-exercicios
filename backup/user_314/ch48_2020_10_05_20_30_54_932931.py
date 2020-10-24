def eh_crescente (l):
    i=0
    c=0

    while (i<(len(l)-1)):
    
        if(l[i+1]>l[i]):
            c+=1

        i+=1

    if (c==(len(l)-1)):
        return True
    else:
        return False