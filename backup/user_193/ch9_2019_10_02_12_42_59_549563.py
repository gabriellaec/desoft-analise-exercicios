def sufixo (a,b):
    i=0
    while i<len(b):
        if a[i] == b[-len(a)] and a[i+1] == b[-len(a)+1]:
            return True
        else:
            return False
        i+=1