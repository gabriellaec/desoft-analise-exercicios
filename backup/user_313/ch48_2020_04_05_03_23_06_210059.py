def eh_crescente(l1):
    c = 0
    i = 1
    while True:
        if l1[i]<l1[c]:
            i+=1
            c+=1
            if i == len(l1):
                return(True)
                
                
        else:
            return(False)