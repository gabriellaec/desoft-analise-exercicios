
def estritamente_crescente(l):
    ec = []
    i = 1
    if len(l) == 0:
        return ec
    else:
        ec.append(l[0])
        while i < len(l):
            if l[i] > ec[-1]:
                ec.append(i)
            i+=1 
        return ec
