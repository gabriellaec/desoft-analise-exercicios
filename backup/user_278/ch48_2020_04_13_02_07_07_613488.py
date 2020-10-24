def eh_crescente(l1):
    if l1 == []:
        return l1
    else:
        inicial = l1 [0]
        for i in range (0,len(l1)-1):
            if l1[i+1] > inicial:
                inicial = l1[i+1]
                return True
            else:
                return False