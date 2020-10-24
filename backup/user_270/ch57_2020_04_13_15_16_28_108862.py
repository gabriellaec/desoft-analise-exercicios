def pa(l):
    n = 0
    r = l[1]-l[0]
    for i in range(1, len(l)):
        if l[i] - l[i-1] = r :
            n += 1
    if n == len(l) - 1 :
        return True
    else:
        return False
def pg(l):
    if l[0] == 0:
        return False
    q = l[1]/l[0]
    n = 0
    for i in range(1, len(l)):
        if l[i]/l[i-1] == q :
            n+=1 
    if n == len(l)-1:
        return True
    else:
        return False
    
def verifica_progressao(l):
    if pa(l) == True and pg == True :
        return "AG"
    elif pa(l) == True:
        return "PA"
    elif pg(l) == True:
        return "PG"
    else:
        return "NA"
    
        
            