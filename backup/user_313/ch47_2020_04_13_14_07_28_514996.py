def estritamente_crescente(l1):
    new = list()
    if len(l1) == 0:
        return l1
    else:
        new.append(l1[0])
        for i in range(1,len(l1)):
            if l1[i] not in new:
                if l1[i] > max(new):
                    new.append(l1[i])
                    
                else:
                    pass
           
    return new