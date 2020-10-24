def eh_crescente(l1):
    if l1 == []:
        return l1
    else:
        i = 0
        inicial = l1 [0]
        while i < (len(l1)-1):
            if l1[i+1] < inicial:
                return False
            else: 
                l1[i+1] > inicial
                inicial = l1[i+1]
                i+=1
            return True