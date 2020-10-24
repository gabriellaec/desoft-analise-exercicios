def eh_crescente(a):
    i = 0
    while i < len(a):
        if a[0] < a[i] and a[i]< a[i+1]:
            i+=1
            return True
        else:
            return False
    return True