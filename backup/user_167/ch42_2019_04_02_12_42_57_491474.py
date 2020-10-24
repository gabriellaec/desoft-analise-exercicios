def quantos_uns(n):
    n=str(n)
    i=1
    s=0
    while i < len(n):
        if n[i]=="1":
        	s+=1
        i+=1
    
    return s