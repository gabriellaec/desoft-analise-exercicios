def eh_crescente(list):
    n = len(list)
   
    i=1
    while i < n-1:
        if list[i-1] < list[i]:
            i=i+1
        else:
            return False
    return True