def eh_crescente(l1):
    if len(l1) == 0 or len(l1) == 1:
        return True
    else:
        for i in range (len(l1)):
            if l1[i+1] <= l1[i]:
                return False
        return True